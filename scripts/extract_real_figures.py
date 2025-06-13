#!/usr/bin/env python3
"""
Extract actual embedded figures from PDF papers, not page screenshots.
This script extracts the real image objects embedded in PDFs.
"""

import os
import fitz  # PyMuPDF
import io
import hashlib
from PIL import Image, ImageStat
import numpy as np
from pathlib import Path
import re

class RealFigureExtractor:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.papers_dir = self.base_dir / "temp_papers"
        self.research_page = self.base_dir / "_pages" / "research.html"
        
        # Create directories
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        
        # Quality thresholds for real scientific figures
        self.min_width = 400
        self.min_height = 300
        self.min_file_size = 20000  # 20KB minimum
        self.max_file_size = 2000000  # 2MB maximum
        
        # Research area keywords for categorization
        self.categories = {
            'foundation-models': ['astromlab', 'eaira', 'llm', 'language', 'ai_model', 'gpt', 'foundation'],
            'machine-learning': ['neural', 'deep', 'learning', 'anomaly', 'detection', 'generative', 'modular'],
            'dark-matter': ['dark', 'matter', 'cosmic', 'web', 'caustic', 'halo', 'cosmology'],
            'emulation-inference': ['emulation', 'probabilistic', 'surrogate', 'bayesian', 'inference', 'uncertainty']
        }
    
    def is_scientific_figure(self, image, file_size):
        """Determine if an extracted image is a scientific figure."""
        width, height = image.size
        
        # Size checks - real figures should be reasonably large
        if width < self.min_width or height < self.min_height:
            return False
        
        # File size checks
        if file_size < self.min_file_size or file_size > self.max_file_size:
            return False
        
        # Aspect ratio check - avoid very thin/wide images (likely UI elements)
        aspect_ratio = width / height
        if aspect_ratio < 0.4 or aspect_ratio > 3.0:
            return False
        
        try:
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Check for reasonable color complexity (scientific figures have detail)
            stat = ImageStat.Stat(image)
            
            # Color variance check - scientific figures should have detail
            variance = np.mean(stat.var)
            if variance < 200:  # Too uniform, likely not a real figure
                return False
            
            # Brightness check
            brightness = np.mean(stat.mean)
            if brightness < 30 or brightness > 220:  # Too dark or too bright
                return False
            
            # Check for reasonable color distribution
            if len(stat.var) >= 3:  # RGB channels
                color_range = max(stat.var) - min(stat.var)
                if color_range < 100:  # Too little color variation
                    return False
        
        except Exception:
            return False
        
        return True
    
    def extract_embedded_figures(self, pdf_path, paper_slug=""):
        """Extract embedded figure objects from PDF, not page screenshots."""
        if not os.path.exists(pdf_path):
            print(f"❌ PDF not found: {pdf_path}")
            return []
        
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"❌ Error opening PDF {pdf_path}: {e}")
            return []
        
        figures = []
        paper_name = paper_slug or Path(pdf_path).stem
        
        print(f"🔍 Extracting embedded figures from: {Path(pdf_path).name}")
        
        # Track unique images to avoid duplicates
        seen_hashes = set()
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Get all image objects on the page
            image_list = page.get_images(full=True)
            
            for img_index, img in enumerate(image_list):
                try:
                    # Extract the image data
                    xref = img[0]
                    
                    # Get image as pixmap
                    pix = fitz.Pixmap(doc, xref)
                    
                    # Skip if image is too small (likely not a scientific figure)
                    if pix.width < self.min_width or pix.height < self.min_height:
                        pix = None
                        continue
                    
                    # Convert CMYK to RGB if needed
                    if pix.n - pix.alpha >= 4:  # CMYK
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    
                    # Get image data
                    img_data = pix.tobytes("png")
                    pix = None
                    
                    # Check for duplicates
                    img_hash = hashlib.md5(img_data).hexdigest()
                    if img_hash in seen_hashes:
                        continue
                    seen_hashes.add(img_hash)
                    
                    # Load with PIL for analysis
                    image = Image.open(io.BytesIO(img_data))
                    
                    # Check if it's a real scientific figure
                    if self.is_scientific_figure(image, len(img_data)):
                        # Create filename
                        short_hash = img_hash[:8]
                        filename = f"{paper_name}_fig{len(figures)+1}_{short_hash}.png"
                        filepath = self.figures_dir / filename
                        
                        # Save image
                        image.save(filepath, "PNG", optimize=True)
                        
                        figure_info = {
                            'filename': filename,
                            'filepath': str(filepath),
                            'paper_slug': paper_name,
                            'page': page_num + 1,
                            'size': image.size,
                            'file_size': len(img_data),
                            'relative_path': f"/images/research/figures/{filename}"
                        }
                        
                        figures.append(figure_info)
                        print(f"  ✅ Extracted figure: {filename} ({image.size[0]}x{image.size[1]})")
                
                except Exception as e:
                    print(f"  ⚠️ Error extracting image {img_index} from page {page_num}: {e}")
                    continue
        
        doc.close()
        print(f"🎉 Extracted {len(figures)} real figures from {Path(pdf_path).name}")
        return figures
    
    def categorize_figure(self, figure_info):
        """Categorize figure based on paper name/content."""
        text = figure_info['paper_slug'].lower()
        
        # Check categories in priority order
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if keyword in text:
                    return category
        
        return 'machine-learning'  # Default category
    
    def select_best_figures_per_category(self, all_figures, max_per_category=2):
        """Select the best 1-2 figures per research category."""
        categorized = {cat: [] for cat in self.categories.keys()}
        
        # Categorize all figures
        for fig in all_figures:
            category = self.categorize_figure(fig)
            categorized[category].append(fig)
        
        # Select best figures for each category
        selected = {}
        for category, figures in categorized.items():
            if not figures:
                selected[category] = []
                continue
            
            # Sort by file size (larger often means higher quality)
            figures.sort(key=lambda x: x['file_size'], reverse=True)
            
            # Take the best ones
            selected[category] = figures[:max_per_category]
            
            print(f"📊 {category}: Selected {len(selected[category])} figures")
            for fig in selected[category]:
                print(f"   - {fig['filename']}")
        
        return selected
    
    def update_research_page(self, selected_figures):
        """Update research page with selected figures."""
        if not self.research_page.exists():
            print(f"❌ Research page not found")
            return False
        
        with open(self.research_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Section mappings
        section_mappings = {
            'foundation-models': 'Foundation Models',
            'machine-learning': 'Machine Learning for Science',
            'dark-matter': 'Dark Matter & Cosmology',
            'emulation-inference': 'Emulation & Inference'
        }
        
        for category, section_title in section_mappings.items():
            figures = selected_figures.get(category, [])
            
            if figures:
                # Create HTML for figures
                figures_html = ""
                for fig in figures:
                    figures_html += f'''        <div class="preview-figure">
          <img src="{fig['relative_path']}" alt="Research preview" onclick="openModal(this)" />
        </div>

'''
                figures_html = figures_html.rstrip() + "\n"
            else:
                # No figures message
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
        
        print(f"✅ Updated research page")
        return True
    
    def process_papers_directory(self):
        """Process all PDFs in the papers directory."""
        if not self.papers_dir.exists():
            print(f"❌ Papers directory not found: {self.papers_dir}")
            return
        
        pdf_files = list(self.papers_dir.glob("*.pdf"))
        if not pdf_files:
            print(f"❌ No PDF files found in {self.papers_dir}")
            return
        
        print(f"🔍 Found {len(pdf_files)} PDF files to process...")
        
        all_figures = []
        
        for pdf_file in pdf_files:
            paper_slug = pdf_file.stem.lower().replace(' ', '_')
            figures = self.extract_embedded_figures(str(pdf_file), paper_slug)
            all_figures.extend(figures)
        
        print(f"\n📊 Total figures extracted: {len(all_figures)}")
        
        if all_figures:
            # Select best figures per category
            selected = self.select_best_figures_per_category(all_figures, max_per_category=2)
            
            # Update research page
            self.update_research_page(selected)
            
            print(f"\n🎉 Research page updated with real scientific figures!")
        else:
            print(f"\n⚠️ No suitable figures found")

def main():
    extractor = RealFigureExtractor()
    extractor.process_papers_directory()

if __name__ == "__main__":
    main()