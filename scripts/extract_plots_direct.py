#!/usr/bin/env python3
"""
Direct plot extraction from available PDF files.
Extract the best/last plot from each available paper.
"""

import os
import fitz  # PyMuPDF
import io
import hashlib
from PIL import Image, ImageStat
import numpy as np
from pathlib import Path
import re

class DirectPlotExtractor:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.papers_dir = self.base_dir / "temp_papers"
        self.research_page = self.base_dir / "_pages" / "research.html"
        
        # Create directories
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        
        # Map filenames to categories
        self.paper_categories = {
            'Application_of_probabilistic_modeling_and_automate.pdf': 'emulation-inference',
            'AstroMLab_3_Achieving_GPT-4o_Level_Performance_in_.pdf': 'foundation-models',
            'AstroMLab_4_Benchmark-Topping_Performance_in_Astro.pdf': 'foundation-models',
            'EAIRA_Establishing_a_Methodology_for_Evaluating_AI.pdf': 'foundation-models',
            'Generative_networks_synthetic_sky_images.pdf': 'machine-learning',
            'Modular_deep_learning_galaxy_scale.pdf': 'machine-learning',
            'Neural_Network_Based_Point_Spread_Function_Deconvo.pdf': 'machine-learning',
            'Probabilistic_neural_network_reduced_order.pdf': 'emulation-inference',
            'The_Caustic_Design_of_the_Dark_Matter_Web.pdf': 'dark-matter'
        }
        
        self.category_names = {
            'foundation-models': 'Foundation Models',
            'machine-learning': 'Machine Learning for Science',
            'dark-matter': 'Dark Matter & Cosmology',
            'emulation-inference': 'Emulation & Inference'
        }
    
    def is_good_scientific_figure(self, image: Image.Image, file_size: int) -> bool:
        """Check if image is a good scientific figure."""
        width, height = image.size
        
        # Size requirements (more lenient)
        if width < 250 or height < 150 or file_size < 8000:
            return False
        
        # Aspect ratio
        aspect_ratio = width / height
        if aspect_ratio < 0.2 or aspect_ratio > 5.0:
            return False
        
        try:
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            stat = ImageStat.Stat(image)
            variance = np.mean(stat.var)
            
            # Scientific figures should have some complexity
            if variance < 50:
                return False
                
        except Exception:
            return False
        
        return True
    
    def extract_best_plot_from_pdf(self, pdf_path: str) -> list:
        """Extract the best plots from a PDF (preferring later pages)."""
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"      ❌ Error opening PDF: {e}")
            return []
        
        paper_name = Path(pdf_path).stem
        print(f"   🔍 Extracting plots from: {paper_name}")
        
        all_figures = []
        seen_hashes = set()
        
        # Scan through ALL pages to find ALL figures
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            image_list = page.get_images(full=True)
            
            for img_index, img in enumerate(image_list):
                try:
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    # Check for duplicates
                    img_hash = hashlib.md5(image_bytes).hexdigest()
                    if img_hash in seen_hashes:
                        continue
                    seen_hashes.add(img_hash)
                    
                    # Load and evaluate the image
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    if self.is_good_scientific_figure(image, len(image_bytes)):
                        # Calculate quality score
                        if image.mode != 'RGB':
                            image_rgb = image.convert('RGB')
                        else:
                            image_rgb = image
                        
                        stat = ImageStat.Stat(image_rgb)
                        complexity = np.mean(stat.var)
                        area = image.size[0] * image.size[1]
                        quality_score = area * complexity
                        
                        # Boost score for later pages (likely better figures)
                        page_boost = page_num * 0.1
                        final_score = quality_score * (1 + page_boost)
                        
                        all_figures.append({
                            'image': image,
                            'image_bytes': image_bytes,
                            'hash': img_hash[:8],
                            'size': image.size,
                            'quality_score': final_score,
                            'page': page_num + 1,
                            'complexity': complexity
                        })
                        
                        print(f"      📊 Found: page {page_num + 1}, {image.size[0]}x{image.size[1]}, score={final_score:.0f}")
                        
                except Exception as e:
                    continue
        
        doc.close()
        
        if not all_figures:
            print(f"      ❌ No suitable figures found")
            return []
        
        # Sort by quality score and return top 3 figures
        all_figures.sort(key=lambda x: x['quality_score'], reverse=True)
        top_figures = all_figures[:3]  # Get top 3 figures
        
        extracted_plots = []
        for i, figure in enumerate(top_figures):
            # Save the figure
            filename = f"{paper_name}_plot_{i+1}_{figure['hash']}.png"
            filepath = self.figures_dir / filename
            
            if figure['image'].mode != 'RGB':
                figure['image'] = figure['image'].convert('RGB')
            figure['image'].save(filepath, "PNG", optimize=True)
            
            plot_info = {
                'filename': filename,
                'paper_title': paper_name.replace('_', ' '),
                'size': figure['size'],
                'page': figure['page'],
                'relative_path': f"/images/research/figures/{filename}",
                'quality_score': figure['quality_score']
            }
            
            extracted_plots.append(plot_info)
            print(f"      ✅ Saved: {filename} (page {figure['page']}, {figure['size'][0]}x{figure['size'][1]})")
        
        return extracted_plots
    
    def extract_all_plots(self):
        """Extract plots from all available PDFs."""
        print("🎨 Extracting plots from available papers...\n")
        
        plots_by_category = {
            'foundation-models': [],
            'machine-learning': [],
            'dark-matter': [],
            'emulation-inference': []
        }
        
        for filename, category in self.paper_categories.items():
            pdf_path = self.papers_dir / filename
            
            if not pdf_path.exists():
                print(f"   ⚠️ Missing: {filename}")
                continue
            
            plots = self.extract_best_plot_from_pdf(str(pdf_path))
            plots_by_category[category].extend(plots)
            print(f"   📈 Extracted {len(plots)} plots for {self.category_names[category]}\n")
        
        return plots_by_category
    
    def update_research_page_with_plots(self, plots_by_category):
        """Update research page with extracted plots."""
        print("📝 Updating research page with plots...")
        
        if not self.research_page.exists():
            print(f"❌ Research page not found")
            return False
        
        with open(self.research_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update each category section
        colors = {
            'foundation-models': '#6366f1',
            'machine-learning': '#3b82f6',
            'dark-matter': '#8b5cf6',
            'emulation-inference': '#f59e0b'
        }
        
        for category, plots in plots_by_category.items():
            category_name = self.category_names[category]
            
            # Select top 2 plots for display
            display_plots = plots[:2]
            
            if display_plots:
                plots_html = ""
                for plot in display_plots:
                    plots_html += f'''        <div class="research-figure">
          <img src="{plot['relative_path']}" alt="Figure from {plot['paper_title']}" onclick="openModal(this)" loading="lazy" />
          <div class="figure-caption">From: {plot['paper_title'][:50]}{'...' if len(plot['paper_title']) > 50 else ''}</div>
        </div>
'''
            else:
                plots_html = '''        <div class="no-figures">
          <p>Representative figures will be added soon.</p>
        </div>
'''
            
            # Find and replace the research figures section
            pattern = rf'({re.escape(category_name)}.*?<div class="research-figures">)(.*?)(</div>\s*</div>\s*<div class="research-stats">)'
            
            def replace_figures(match):
                before = match.group(1)
                after = match.group(3)
                return f"{before}\n{plots_html}      {after}"
            
            content = re.sub(pattern, replace_figures, content, flags=re.DOTALL)
            
            # Update figure count in stats
            stats_pattern = rf'(<span class="stat">)(\d+)( Figures Available</span>)'
            content = re.sub(stats_pattern, rf'\g<1>{len(plots)}\g<3>', content)
        
        # Write updated content
        with open(self.research_page, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Research page updated with plots")
        return True
    
    def run(self):
        """Run the plot extraction and page update."""
        print("🚀 Direct Plot Extraction from Available Papers\n")
        print("=" * 50)
        
        # Extract plots from all available PDFs
        plots_by_category = self.extract_all_plots()
        
        # Update research page
        self.update_research_page_with_plots(plots_by_category)
        
        # Summary
        print("\n" + "=" * 50)
        print("🎉 PLOT EXTRACTION COMPLETE!")
        print("=" * 50)
        
        total_plots = sum(len(plots) for plots in plots_by_category.values())
        print(f"\n📊 Summary:")
        print(f"   🎨 Total plots extracted: {total_plots}")
        
        for category, plots in plots_by_category.items():
            if plots:
                print(f"   {self.category_names[category]}: {len(plots)} plots")
        
        print(f"\n✨ Research page now displays real scientific figures from YOUR papers!")

def main():
    extractor = DirectPlotExtractor()
    extractor.run()

if __name__ == "__main__":
    main()