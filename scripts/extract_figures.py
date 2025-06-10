#!/usr/bin/env python3
"""
Figure extraction script for academic papers.
Extracts high-quality figures from PDFs and organizes them for the research portfolio.
"""

import os
import fitz  # PyMuPDF
import io
import hashlib
from PIL import Image, ImageStat
import numpy as np
import requests
import re
from typing import List, Dict, Tuple
import json
from urllib.parse import urlparse

class FigureExtractor:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.images_dir = os.path.join(self.base_dir, "images", "research")
        self.figures_dir = os.path.join(self.images_dir, "figures")
        
        # Create directories
        os.makedirs(self.images_dir, exist_ok=True)
        os.makedirs(self.figures_dir, exist_ok=True)
        
        # Figure quality thresholds
        self.min_width = 300
        self.min_height = 200
        self.min_file_size = 10000  # 10KB
        self.max_file_size = 2000000  # 2MB
        
    def is_good_figure(self, image: Image.Image, file_size: int) -> bool:
        """Determine if an image is a good scientific figure."""
        width, height = image.size
        
        # Size checks
        if width < self.min_width or height < self.min_height:
            return False
        
        if file_size < self.min_file_size or file_size > self.max_file_size:
            return False
        
        # Aspect ratio check (avoid very thin/wide images)
        aspect_ratio = width / height
        if aspect_ratio < 0.3 or aspect_ratio > 4.0:
            return False
        
        # Color complexity check (avoid simple images)
        try:
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Calculate image statistics
            stat = ImageStat.Stat(image)
            
            # Check for reasonable color variance
            variance = np.mean(stat.var)
            if variance < 100:  # Too uniform
                return False
            
            # Check for reasonable brightness
            brightness = np.mean(stat.mean)
            if brightness < 20 or brightness > 235:  # Too dark or too bright
                return False
            
        except Exception:
            return False
        
        return True
    
    def extract_from_pdf(self, pdf_path: str, paper_title: str = "") -> List[Dict]:
        """Extract figures from a PDF file."""
        if not os.path.exists(pdf_path):
            print(f"PDF not found: {pdf_path}")
            return []
        
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"Error opening PDF {pdf_path}: {e}")
            return []
        
        figures = []
        paper_slug = self.create_slug(paper_title) if paper_title else os.path.splitext(os.path.basename(pdf_path))[0]
        
        print(f"Processing PDF: {os.path.basename(pdf_path)}")
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                try:
                    # Extract image
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    
                    # Skip if CMYK (convert to RGB)
                    if pix.n - pix.alpha < 4:
                        img_data = pix.tobytes("png")
                        pix = None
                    else:
                        # Convert CMYK to RGB
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                        img_data = pix.tobytes("png")
                        pix = None
                    
                    # Load with PIL for analysis
                    image = Image.open(io.BytesIO(img_data))
                    
                    # Check if it's a good figure
                    if self.is_good_figure(image, len(img_data)):
                        # Create filename
                        img_hash = hashlib.md5(img_data).hexdigest()[:8]
                        filename = f"{paper_slug}_page{page_num+1}_fig{img_index+1}_{img_hash}.png"
                        filepath = os.path.join(self.figures_dir, filename)
                        
                        # Save image
                        image.save(filepath, "PNG", optimize=True)
                        
                        figure_info = {
                            'filename': filename,
                            'filepath': filepath,
                            'paper_title': paper_title,
                            'paper_slug': paper_slug,
                            'page': page_num + 1,
                            'size': image.size,
                            'file_size': len(img_data),
                            'relative_path': f"/images/research/figures/{filename}"
                        }
                        
                        figures.append(figure_info)
                        print(f"  Extracted figure: {filename} ({image.size[0]}x{image.size[1]})")
                
                except Exception as e:
                    print(f"  Error extracting image {img_index} from page {page_num}: {e}")
                    continue
        
        doc.close()
        print(f"Extracted {len(figures)} figures from {os.path.basename(pdf_path)}")
        return figures
    
    def download_pdf_from_url(self, url: str, title: str = "") -> str:
        """Download a PDF from a URL."""
        try:
            # Handle arXiv URLs - convert to PDF download URL
            if "arxiv.org/abs/" in url:
                arxiv_id = url.split("/abs/")[-1].split("v")[0]  # Remove version
                url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                print(f"Converted arXiv URL to PDF: {url}")
            
            # Create filename from title or URL
            if title:
                filename = self.create_slug(title) + ".pdf"
            else:
                parsed = urlparse(url)
                filename = os.path.basename(parsed.path) or "paper.pdf"
                if not filename.endswith('.pdf'):
                    filename += '.pdf'
            
            temp_dir = os.path.join(self.base_dir, "temp_papers")
            filepath = os.path.join(temp_dir, filename)
            os.makedirs(temp_dir, exist_ok=True)
            
            print(f"Downloading PDF from: {url}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, stream=True, timeout=60)
            response.raise_for_status()
            
            # Check if it's actually a PDF
            content_type = response.headers.get('content-type', '').lower()
            if 'pdf' not in content_type and not url.endswith('.pdf'):
                print(f"Warning: URL may not be a PDF (content-type: {content_type})")
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Downloaded: {filename} ({os.path.getsize(filepath)} bytes)")
            return filepath
            
        except Exception as e:
            print(f"Error downloading PDF from {url}: {e}")
            return ""
    
    def create_slug(self, text: str) -> str:
        """Create a URL-friendly slug."""
        slug = text.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'\s+', '_', slug)
        return slug[:50]
    
    def categorize_figure(self, figure_info: Dict, paper_info: Dict) -> str:
        """Determine which research category a figure belongs to."""
        paper_text = (paper_info.get('title', '') + ' ' + 
                     paper_info.get('abstract', '') + ' ' + 
                     paper_info.get('venue', '')).lower()
        
        # Keywords for different categories
        categories = {
            'machine-learning': ['machine learning', 'deep learning', 'neural network', 'ai ', 'artificial intelligence', 'model', 'training'],
            'dark-matter': ['dark matter', 'cosmic web', 'cosmology', 'halo', 'structure formation', 'n-body', 'simulation'],
            'uncertainty-quantification': ['uncertainty', 'bayesian', 'probabilistic', 'error', 'confidence'],
            'gravitational-lensing': ['gravitational lens', 'strong lens', 'weak lens', 'lensing', 'shear'],
            'other-research': []
        }
        
        for category, keywords in categories.items():
            if category == 'other-research':
                continue
            for keyword in keywords:
                if keyword in paper_text:
                    return category
        
        return 'other-research'
    
    def get_paper_info_from_title(self, title: str) -> Dict:
        """Get paper information from the publications directory."""
        pub_dir = os.path.join(self.base_dir, "_publications")
        
        for filename in os.listdir(pub_dir):
            if not filename.endswith('.md'):
                continue
            
            try:
                with open(os.path.join(pub_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract title from YAML front matter
                title_match = re.search(r'title:\s*["\'](.*?)["\']', content, re.DOTALL)
                if title_match:
                    file_title = title_match.group(1)
                    # Check if titles match (fuzzy matching)
                    if self.titles_match(title, file_title):
                        # Extract other metadata
                        venue_match = re.search(r'venue:\s*["\'](.*?)["\']', content)
                        
                        # Extract abstract/summary
                        summary_match = re.search(r'---\s*\n\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
                        
                        return {
                            'title': file_title,
                            'venue': venue_match.group(1) if venue_match else '',
                            'abstract': summary_match.group(1).strip() if summary_match else '',
                            'filename': filename
                        }
            except Exception as e:
                continue
        
        return {'title': title, 'venue': '', 'abstract': ''}
    
    def titles_match(self, title1: str, title2: str) -> bool:
        """Check if two titles are similar enough to be the same paper."""
        # Normalize titles
        t1 = re.sub(r'[^\w\s]', '', title1.lower())
        t2 = re.sub(r'[^\w\s]', '', title2.lower())
        
        # Simple word overlap check
        words1 = set(t1.split())
        words2 = set(t2.split())
        
        if len(words1) == 0 or len(words2) == 0:
            return False
        
        overlap = len(words1.intersection(words2))
        min_words = min(len(words1), len(words2))
        
        return overlap / min_words > 0.7  # 70% word overlap
    
    def update_research_with_figures(self, figures_by_category: Dict[str, List[Dict]]):
        """Update research portfolio files with extracted figures."""
        portfolio_dir = os.path.join(self.base_dir, "_portfolio")
        
        category_files = {
            'machine-learning': 'portfolio-1-machine-learning.md',
            'dark-matter': 'portfolio-2-dark-matter.md', 
            'uncertainty-quantification': 'portfolio-3-uncertainty-quantification.md',
            'gravitational-lensing': 'portfolio-4-gravitational-lensing.md',
            'other-research': 'portfolio-5-other-research.md'
        }
        
        for category, figures in figures_by_category.items():
            if not figures:
                continue
            
            portfolio_file = category_files.get(category)
            if not portfolio_file:
                continue
            
            filepath = os.path.join(portfolio_dir, portfolio_file)
            
            if not os.path.exists(filepath):
                continue
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find the end of the front matter
                yaml_end = content.find('---', 3) + 3
                
                if yaml_end < 3:
                    continue
                
                front_matter = content[:yaml_end]
                body = content[yaml_end:].strip()
                
                # Add figures section
                figures_html = self.create_figures_html(figures)
                
                # Look for existing figures section
                if "## Research Figures" in body:
                    # Replace existing figures section
                    pattern = r'## Research Figures.*?(?=\n## |$)'
                    body = re.sub(pattern, f"## Research Figures\n\n{figures_html}", body, flags=re.DOTALL)
                else:
                    # Add new figures section before publications
                    if "## Related Publications" in body:
                        body = body.replace("## Related Publications", f"## Research Figures\n\n{figures_html}\n\n## Related Publications")
                    else:
                        body += f"\n\n## Research Figures\n\n{figures_html}"
                
                # Write updated content
                updated_content = front_matter + "\n\n" + body
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                print(f"Updated {portfolio_file} with {len(figures)} figures")
                
            except Exception as e:
                print(f"Error updating {portfolio_file}: {e}")
    
    def create_figures_html(self, figures: List[Dict]) -> str:
        """Create HTML for displaying figures in a grid."""
        if not figures:
            return "No figures available for this research area.\n"
        
        html = '<div class="research-figures-grid">\n'
        
        for fig in figures[:6]:  # Limit to 6 figures per category
            html += f'''  <div class="research-figure">
    <img src="{fig['relative_path']}" alt="Figure from {fig['paper_title']}" onclick="openModal(this)">
    <p class="figure-caption">From: {fig['paper_title'][:80]}{'...' if len(fig['paper_title']) > 80 else ''}</p>
  </div>
'''
        
        html += '</div>\n'
        
        # Add modal and CSS if not already present
        html += '''
<style>
.research-figures-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.research-figure {
  text-align: center;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  transition: transform 0.2s ease;
}

.research-figure:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.research-figure img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.research-figure img:hover {
  opacity: 0.9;
}

.figure-caption {
  font-size: 0.85em;
  color: #6c757d;
  margin-top: 0.5rem;
  line-height: 1.3;
}

/* Modal styles */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  padding-top: 5%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}
</style>

<div id="imageModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="modalImage">
</div>

<script>
function openModal(img) {
  var modal = document.getElementById('imageModal');
  var modalImg = document.getElementById('modalImage');
  modal.style.display = 'block';
  modalImg.src = img.src;
}

function closeModal() {
  document.getElementById('imageModal').style.display = 'none';
}

// Close modal when clicking outside the image
window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}
</script>
'''
        
        return html

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract figures from academic papers')
    parser.add_argument('action', choices=['extract-local', 'extract-url', 'update-portfolio'], 
                       help='Action to perform')
    parser.add_argument('--pdf', help='Path to PDF file (for extract-local)')
    parser.add_argument('--url', help='URL to PDF (for extract-url)')
    parser.add_argument('--title', help='Paper title')
    
    args = parser.parse_args()
    
    extractor = FigureExtractor()
    
    if args.action == 'extract-local':
        if not args.pdf:
            print("Error: --pdf is required for extract-local")
            return
        
        figures = extractor.extract_from_pdf(args.pdf, args.title or "")
        
        if figures:
            # Categorize figures
            paper_info = extractor.get_paper_info_from_title(args.title or "")
            figures_by_category = {}
            
            for fig in figures:
                category = extractor.categorize_figure(fig, paper_info)
                if category not in figures_by_category:
                    figures_by_category[category] = []
                figures_by_category[category].append(fig)
            
            # Update portfolio
            extractor.update_research_with_figures(figures_by_category)
            
            print(f"\nFigures extracted and categorized:")
            for cat, figs in figures_by_category.items():
                print(f"  {cat}: {len(figs)} figures")
    
    elif args.action == 'extract-url':
        if not args.url:
            print("Error: --url is required for extract-url")
            return
        
        # Download PDF
        pdf_path = extractor.download_pdf_from_url(args.url, args.title or "")
        if pdf_path:
            # Extract figures
            figures = extractor.extract_from_pdf(pdf_path, args.title or "")
            
            if figures:
                # Process similar to local extraction
                paper_info = extractor.get_paper_info_from_title(args.title or "")
                figures_by_category = {}
                
                for fig in figures:
                    category = extractor.categorize_figure(fig, paper_info)
                    if category not in figures_by_category:
                        figures_by_category[category] = []
                    figures_by_category[category].append(fig)
                
                extractor.update_research_with_figures(figures_by_category)
                
                print(f"\nFigures extracted and categorized:")
                for cat, figs in figures_by_category.items():
                    print(f"  {cat}: {len(figs)} figures")
            
            # Clean up downloaded file
            try:
                os.remove(pdf_path)
            except:
                pass
    
    elif args.action == 'update-portfolio':
        # Process existing figures
        print("Updating portfolio with existing figures...")
        # This would scan the figures directory and update portfolios

if __name__ == "__main__":
    main()