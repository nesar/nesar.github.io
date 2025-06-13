#!/usr/bin/env python3
"""
Maintenance script for research plots.
This script can be run regularly to extract figures from new papers
and update the research page with real scientific figures.
"""

import os
import fitz  # PyMuPDF
import io
import hashlib
from PIL import Image, ImageStat
import numpy as np
from pathlib import Path
import re

class ResearchPlotMaintainer:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.papers_dir = self.base_dir / "temp_papers"
        self.research_page = self.base_dir / "_pages" / "research.html"
        
        # Create directories
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        
        # Quality thresholds for real scientific figures
        self.min_width = 200
        self.min_height = 150
        self.min_file_size = 5000
        self.max_file_size = 5000000
    
    def is_scientific_figure(self, image, file_size):
        """Check if an image is likely a scientific figure."""
        width, height = image.size
        
        # Basic size and file size checks
        if (width < self.min_width or height < self.min_height or 
            file_size < self.min_file_size or file_size > self.max_file_size):
            return False
        
        # Aspect ratio check
        aspect_ratio = width / height
        if aspect_ratio < 0.2 or aspect_ratio > 5.0:
            return False
        
        try:
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            stat = ImageStat.Stat(image)
            variance = np.mean(stat.var)
            
            # Complexity check - scientific figures should have some detail
            if variance < 50:
                return False
                
        except Exception:
            pass
        
        return True
    
    def extract_figures_from_pdf(self, pdf_path):
        """Extract embedded figures from a PDF."""
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"❌ Error opening {pdf_path}: {e}")
            return []
        
        extracted_figures = []
        paper_name = Path(pdf_path).stem
        seen_hashes = set()
        
        print(f"🔍 Processing {paper_name}...")
        
        for page_num in range(min(len(doc), 10)):  # Check first 10 pages
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
                    
                    # Load and check the image
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    if self.is_scientific_figure(image, len(image_bytes)):
                        # Save the figure
                        short_hash = img_hash[:8]
                        filename = f"{paper_name}_fig{len(extracted_figures)+1}_{short_hash}.png"
                        filepath = self.figures_dir / filename
                        
                        if image.mode != 'RGB':
                            image = image.convert('RGB')
                        image.save(filepath, "PNG", optimize=True)
                        
                        figure_info = {
                            'filename': filename,
                            'paper_slug': paper_name,
                            'size': image.size,
                            'relative_path': f"/images/research/figures/{filename}"
                        }
                        
                        extracted_figures.append(figure_info)
                        print(f"  ✅ Extracted: {filename} ({image.size[0]}x{image.size[1]})")
                        
                except Exception as e:
                    continue
        
        doc.close()
        return extracted_figures
    
    def categorize_figures(self, figures):
        """Categorize figures by research area."""
        categories = {
            'foundation-models': ['astromlab', 'eaira', 'llm', 'language', 'foundation', 'ai_methodology'],
            'machine-learning': ['neural', 'deep', 'learning', 'modular', 'constructing', 'impactful', 'anomaly'],
            'dark-matter': ['dark', 'matter', 'cosmic', 'caustic', 'topology', 'halo'],
            'emulation-inference': ['emulation', 'probabilistic', 'generative', 'networks', 'surrogate', 'inference']
        }
        
        categorized = {cat: [] for cat in categories.keys()}
        
        for fig in figures:
            text = fig['paper_slug'].lower()
            
            category_found = False
            for category, keywords in categories.items():
                for keyword in keywords:
                    if keyword in text:
                        categorized[category].append(fig)
                        category_found = True
                        break
                if category_found:
                    break
            
            if not category_found:
                categorized['machine-learning'].append(fig)
        
        return categorized
    
    def select_best_figures(self, categorized, max_per_category=2):
        """Select the best 1-2 figures per category."""
        selected = {}
        
        for category, figures in categorized.items():
            if figures:
                # Sort by image area (larger often means better quality)
                figures.sort(key=lambda x: x['size'][0] * x['size'][1], reverse=True)
                selected[category] = figures[:max_per_category]
            else:
                selected[category] = []
        
        return selected
    
    def update_research_page(self, selected_figures):
        """Update the research page with the selected figures."""
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
                figures_html = ""
                for fig in figures:
                    figures_html += f'''        <div class="preview-figure">
          <img src="{fig['relative_path']}" alt="Research preview" onclick="openModal(this)" />
        </div>

'''
                figures_html = figures_html.rstrip() + "\n"
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
    
    def run_maintenance(self):
        """Run the full maintenance process."""
        print("🔧 Running research plots maintenance...")
        
        if not self.papers_dir.exists():
            print(f"❌ Papers directory not found: {self.papers_dir}")
            print("   Place PDF files in temp_papers/ directory to extract figures")
            return
        
        pdf_files = list(self.papers_dir.glob("*.pdf"))
        if not pdf_files:
            print(f"❌ No PDF files found in {self.papers_dir}")
            return
        
        print(f"📚 Found {len(pdf_files)} PDF files")
        
        # Extract figures from all PDFs
        all_figures = []
        for pdf_file in pdf_files:
            figures = self.extract_figures_from_pdf(str(pdf_file))
            all_figures.extend(figures)
        
        if not all_figures:
            print("⚠️ No figures could be extracted from the PDFs")
            return
        
        print(f"\n📊 Extracted {len(all_figures)} total figures")
        
        # Categorize and select best figures
        categorized = self.categorize_figures(all_figures)
        selected = self.select_best_figures(categorized, max_per_category=2)
        
        # Print summary
        print(f"\n📋 Selected figures by category:")
        total_selected = 0
        for category, figures in selected.items():
            print(f"  {category}: {len(figures)} figures")
            total_selected += len(figures)
            for fig in figures:
                print(f"    - {fig['filename']}")
        
        # Update research page
        if self.update_research_page(selected):
            print(f"\n🎉 Research page updated with {total_selected} real scientific figures!")
        else:
            print(f"\n❌ Failed to update research page")

def main():
    maintainer = ResearchPlotMaintainer()
    maintainer.run_maintenance()

if __name__ == "__main__":
    main()