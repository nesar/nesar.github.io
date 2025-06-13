#!/usr/bin/env python3
"""
Extract exactly 1 figure per paper and update research page.
This ensures diversity across different papers rather than multiple from same paper.
"""

import os
import fitz  # PyMuPDF
import io
import hashlib
from PIL import Image, ImageStat
import numpy as np
from pathlib import Path
import re

class OneFigurePerPaper:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.papers_dir = self.base_dir / "temp_papers"
        self.research_page = self.base_dir / "_pages" / "research.html"
        
        # Quality thresholds for real scientific figures
        self.min_width = 300
        self.min_height = 200
        self.min_file_size = 10000
        self.max_file_size = 5000000
    
    def is_scientific_figure(self, image, file_size):
        """Check if an image is a high-quality scientific figure."""
        width, height = image.size
        
        if (width < self.min_width or height < self.min_height or 
            file_size < self.min_file_size or file_size > self.max_file_size):
            return False
        
        aspect_ratio = width / height
        if aspect_ratio < 0.3 or aspect_ratio > 4.0:
            return False
        
        try:
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            stat = ImageStat.Stat(image)
            variance = np.mean(stat.var)
            
            # Scientific figures should have good detail/complexity
            if variance < 100:
                return False
                
        except Exception:
            pass
        
        return True
    
    def extract_best_figure_from_pdf(self, pdf_path):
        """Extract the BEST single figure from a PDF."""
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"❌ Error opening {pdf_path}: {e}")
            return None
        
        paper_name = Path(pdf_path).stem
        print(f"🔍 Finding best figure from: {paper_name}")
        
        candidate_figures = []
        seen_hashes = set()
        
        # Scan through the paper for figures
        for page_num in range(min(len(doc), 15)):  # Check first 15 pages
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
                    
                    if self.is_scientific_figure(image, len(image_bytes)):
                        # Calculate quality score (size * complexity)
                        if image.mode != 'RGB':
                            image_rgb = image.convert('RGB')
                        else:
                            image_rgb = image
                        
                        stat = ImageStat.Stat(image_rgb)
                        complexity = np.mean(stat.var)
                        area = image.size[0] * image.size[1]
                        quality_score = area * complexity
                        
                        candidate_figures.append({
                            'image': image,
                            'image_bytes': image_bytes,
                            'hash': img_hash[:8],
                            'size': image.size,
                            'quality_score': quality_score,
                            'page': page_num + 1,
                            'complexity': complexity
                        })
                        
                        print(f"  📊 Found candidate: {image.size[0]}x{image.size[1]}, quality={quality_score:.0f}")
                        
                except Exception as e:
                    continue
        
        doc.close()
        
        if not candidate_figures:
            print(f"  ❌ No suitable figures found in {paper_name}")
            return None
        
        # Select the best figure (highest quality score)
        best_figure = max(candidate_figures, key=lambda x: x['quality_score'])
        
        # Save the best figure
        filename = f"{paper_name}_best_fig_{best_figure['hash']}.png"
        filepath = self.figures_dir / filename
        
        if best_figure['image'].mode != 'RGB':
            best_figure['image'] = best_figure['image'].convert('RGB')
        best_figure['image'].save(filepath, "PNG", optimize=True)
        
        figure_info = {
            'filename': filename,
            'paper_slug': paper_name,
            'size': best_figure['size'],
            'relative_path': f"/images/research/figures/{filename}",
            'quality_score': best_figure['quality_score'],
            'page': best_figure['page']
        }
        
        print(f"  ✅ Selected BEST figure: {filename} ({best_figure['size'][0]}x{best_figure['size'][1]}, page {best_figure['page']})")
        return figure_info
    
    def categorize_figure(self, figure_info):
        """Categorize figure by research area based on paper name."""
        text = figure_info['paper_slug'].lower()
        
        categories = {
            'foundation-models': ['astromlab', 'eaira', 'llm', 'language', 'foundation', 'ai_methodology'],
            'machine-learning': ['neural', 'deconvo', 'point_spread', 'deep', 'learning', 'modular'],
            'dark-matter': ['dark', 'matter', 'cosmic', 'caustic', 'topology', 'halo'],
            'emulation-inference': ['probabilistic', 'emulation', 'surrogate', 'application_of_probabilistic']
        }
        
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in text:
                    return category
        
        return 'machine-learning'  # Default
    
    def update_research_page(self, selected_figures):
        """Update research page with exactly 1 figure per category."""
        if not self.research_page.exists():
            print(f"❌ Research page not found")
            return False
        
        with open(self.research_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        section_mappings = {
            'foundation-models': 'Foundation Models',
            'machine-learning': 'Machine Learning for Science',
            'dark-matter': 'Dark Matter & Cosmology',
            'emulation-inference': 'Emulation & Inference'
        }
        
        for category, section_title in section_mappings.items():
            figures = selected_figures.get(category, [])
            
            if figures:
                # Show only 1 figure
                fig = figures[0]
                figures_html = f'''        <div class="preview-figure">
          <img src="{fig['relative_path']}" alt="Research preview" onclick="openModal(this)" />
        </div>

'''
            else:
                figures_html = '''        <div class="no-figures">
          <p>Representative figures coming soon...</p>
        </div>

'''
            
            # Update the section
            pattern = rf'(<a href="[^"]*" class="research-title">{re.escape(section_title)}</a>.*?<div class="research-preview-figures">\s*)(.*?)(\s*</div>\s*</div>)'
            
            def replace_figures(match):
                before = match.group(1)
                after = match.group(3)
                return f"{before}\n{figures_html}{after}"
            
            content = re.sub(pattern, replace_figures, content, flags=re.DOTALL)
        
        # Write updated content
        with open(self.research_page, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    def run(self):
        """Extract 1 best figure per paper and update research page."""
        print("🎯 Extracting 1 BEST figure per paper...\n")
        
        if not self.papers_dir.exists():
            print(f"❌ Papers directory not found: {self.papers_dir}")
            return
        
        pdf_files = list(self.papers_dir.glob("*.pdf"))
        if not pdf_files:
            print(f"❌ No PDF files found in {self.papers_dir}")
            return
        
        print(f"📚 Processing {len(pdf_files)} papers (1 figure each)...")
        
        # Extract best figure from each paper
        all_figures = []
        for pdf_file in pdf_files:
            best_figure = self.extract_best_figure_from_pdf(str(pdf_file))
            if best_figure:
                all_figures.append(best_figure)
        
        print(f"\n📊 Extracted {len(all_figures)} figures total (1 per paper)")
        
        if not all_figures:
            print("❌ No figures could be extracted")
            return
        
        # Categorize figures
        categorized = {
            'foundation-models': [],
            'machine-learning': [],
            'dark-matter': [],
            'emulation-inference': []
        }
        
        for fig in all_figures:
            category = self.categorize_figure(fig)
            categorized[category].append(fig)
        
        # Select 1 best figure per category
        selected = {}
        for category, figures in categorized.items():
            if figures:
                # Sort by quality and take the best one
                figures.sort(key=lambda x: x['quality_score'], reverse=True)
                selected[category] = [figures[0]]  # Only 1 figure
            else:
                selected[category] = []
        
        # Print results
        print(f"\n📋 FINAL SELECTION (1 figure per research area):")
        total_selected = 0
        for category, figures in selected.items():
            if figures:
                fig = figures[0]
                print(f"  {category}: {fig['filename']} (from {fig['paper_slug']})")
                total_selected += 1
            else:
                print(f"  {category}: No figures available")
        
        # Update research page
        if self.update_research_page(selected):
            print(f"\n🎉 Research page updated with {total_selected} figures (1 per research area, 1 per paper)!")
        else:
            print(f"\n❌ Failed to update research page")

def main():
    extractor = OneFigurePerPaper()
    extractor.run()

if __name__ == "__main__":
    main()