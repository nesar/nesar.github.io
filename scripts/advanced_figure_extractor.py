#!/usr/bin/env python3
"""
Advanced figure extraction that can handle different PDF encoding methods.
This script tries multiple approaches to extract real scientific figures.
"""

import os
import fitz  # PyMuPDF
import io
import hashlib
from PIL import Image, ImageStat
import numpy as np
from pathlib import Path
import re

class AdvancedFigureExtractor:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.papers_dir = self.base_dir / "temp_papers"
        self.research_page = self.base_dir / "_pages" / "research.html"
        
        # Create directories
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        
        # More lenient quality thresholds
        self.min_width = 200
        self.min_height = 150
        self.min_file_size = 5000   # 5KB minimum
        self.max_file_size = 5000000  # 5MB maximum
    
    def is_likely_figure(self, image, file_size):
        """More lenient check for scientific figures."""
        width, height = image.size
        
        # Basic size checks
        if width < self.min_width or height < self.min_height:
            return False
        
        if file_size < self.min_file_size or file_size > self.max_file_size:
            return False
        
        # More permissive aspect ratio
        aspect_ratio = width / height
        if aspect_ratio < 0.2 or aspect_ratio > 5.0:
            return False
        
        try:
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            stat = ImageStat.Stat(image)
            
            # Very basic complexity check
            variance = np.mean(stat.var)
            if variance < 50:  # Very uniform image
                return False
                
        except Exception:
            pass
        
        return True
    
    def extract_all_images_debug(self, pdf_path):
        """Extract all images with debug info to understand PDF structure."""
        print(f"\n🔍 DEBUG: Analyzing PDF structure of {Path(pdf_path).name}")
        
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"❌ Error opening PDF: {e}")
            return []
        
        total_images = 0
        extracted_figures = []
        
        for page_num in range(min(len(doc), 5)):  # Check first 5 pages
            page = doc.load_page(page_num)
            image_list = page.get_images(full=True)
            
            print(f"  📄 Page {page_num + 1}: Found {len(image_list)} image objects")
            
            for img_index, img in enumerate(image_list):
                try:
                    xref = img[0]
                    bbox = img[1:5] if len(img) > 4 else None
                    
                    # Get image info
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    print(f"    🖼️ Image {img_index + 1}: {len(image_bytes)} bytes, format: {image_ext}")
                    
                    # Try to load the image
                    image = Image.open(io.BytesIO(image_bytes))
                    width, height = image.size
                    
                    print(f"       Size: {width}x{height}, Mode: {image.mode}")
                    
                    # Check if it might be a figure
                    if self.is_likely_figure(image, len(image_bytes)):
                        # Create filename
                        paper_name = Path(pdf_path).stem
                        img_hash = hashlib.md5(image_bytes).hexdigest()[:8]
                        filename = f"{paper_name}_extracted_fig{total_images + 1}_{img_hash}.png"
                        filepath = self.figures_dir / filename
                        
                        # Save as PNG
                        if image.mode != 'RGB':
                            image = image.convert('RGB')
                        image.save(filepath, "PNG", optimize=True)
                        
                        figure_info = {
                            'filename': filename,
                            'filepath': str(filepath),
                            'paper_slug': paper_name,
                            'page': page_num + 1,
                            'size': (width, height),
                            'file_size': len(image_bytes),
                            'relative_path': f"/images/research/figures/{filename}",
                            'format': image_ext
                        }
                        
                        extracted_figures.append(figure_info)
                        total_images += 1
                        print(f"       ✅ EXTRACTED as {filename}")
                    else:
                        print(f"       ❌ Rejected (size/quality)")
                        
                except Exception as e:
                    print(f"       ⚠️ Error processing image: {e}")
                    continue
        
        doc.close()
        print(f"  📊 Total extracted from {Path(pdf_path).name}: {len(extracted_figures)}")
        return extracted_figures
    
    def categorize_and_select(self, all_figures):
        """Categorize figures and select 1-2 per category."""
        categories = {
            'foundation-models': ['astromlab', 'eaira', 'llm', 'language', 'foundation'],
            'machine-learning': ['neural', 'deep', 'learning', 'modular', 'constructing', 'impactful'],
            'dark-matter': ['dark', 'matter', 'cosmic', 'caustic', 'topology'],
            'emulation-inference': ['emulation', 'probabilistic', 'generative', 'synthetic', 'networks']
        }
        
        categorized = {cat: [] for cat in categories.keys()}
        
        # Categorize figures
        for fig in all_figures:
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
                categorized['machine-learning'].append(fig)  # Default
        
        # Select best figures (by size as quality proxy)
        selected = {}
        for category, figures in categorized.items():
            if figures:
                # Sort by image area (larger usually better quality)
                figures.sort(key=lambda x: x['size'][0] * x['size'][1], reverse=True)
                selected[category] = figures[:2]  # Max 2 per category
            else:
                selected[category] = []
        
        return selected
    
    def update_research_page_simple(self, selected_figures):
        """Update research page with 1-2 figures per section."""
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
            
            # Replace figures section
            pattern = rf'(<a href="[^"]*" class="research-title">{re.escape(section_title)}</a>.*?<div class="research-preview-figures">\s*)(.*?)(\s*</div>\s*</div>)'
            
            def replace_figures(match):
                before = match.group(1)
                after = match.group(3)
                return f"{before}\n{figures_html}{after}"
            
            content = re.sub(pattern, replace_figures, content, flags=re.DOTALL)
        
        with open(self.research_page, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated research page")
        return True
    
    def process_all_pdfs(self):
        """Process all PDFs and extract real figures."""
        if not self.papers_dir.exists():
            print(f"❌ Papers directory not found: {self.papers_dir}")
            return
        
        pdf_files = list(self.papers_dir.glob("*.pdf"))
        if not pdf_files:
            print(f"❌ No PDF files found in {self.papers_dir}")
            return
        
        print(f"🚀 Processing {len(pdf_files)} PDFs for figure extraction...")
        
        all_figures = []
        
        for pdf_file in pdf_files:
            figures = self.extract_all_images_debug(str(pdf_file))
            all_figures.extend(figures)
        
        print(f"\n📊 TOTAL FIGURES EXTRACTED: {len(all_figures)}")
        
        if all_figures:
            # Categorize and select best figures
            selected = self.categorize_and_select(all_figures)
            
            print(f"\n📋 SELECTED FIGURES BY CATEGORY:")
            for category, figures in selected.items():
                print(f"  {category}: {len(figures)} figures")
                for fig in figures:
                    print(f"    - {fig['filename']} ({fig['size'][0]}x{fig['size'][1]})")
            
            # Update research page
            self.update_research_page_simple(selected)
            
            print(f"\n🎉 SUCCESS: Research page updated with {sum(len(figs) for figs in selected.values())} real scientific figures!")
        else:
            print(f"\n❌ No figures could be extracted from the PDFs")

def main():
    extractor = AdvancedFigureExtractor()
    extractor.process_all_pdfs()

if __name__ == "__main__":
    main()