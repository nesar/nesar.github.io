#!/usr/bin/env python3
"""
Alternative figure extraction using pdf2image and PIL.
More robust for extracting figures from academic papers, especially Foundation Models papers.
"""

import os
import hashlib
from PIL import Image, ImageStat
import numpy as np
import requests
import re
from typing import List, Dict, Tuple
import json
from urllib.parse import urlparse
import tempfile
import subprocess

class ImprovedFigureExtractor:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.images_dir = os.path.join(self.base_dir, "images", "research")
        self.figures_dir = os.path.join(self.images_dir, "figures")
        
        # Create directories
        os.makedirs(self.images_dir, exist_ok=True)
        os.makedirs(self.figures_dir, exist_ok=True)
        
        # Figure quality thresholds
        self.min_width = 200
        self.min_height = 150
        self.min_file_size = 5000  # 5KB
        self.max_file_size = 3000000  # 3MB
        
    def check_dependencies(self):
        """Check if required tools are available."""
        try:
            # Check for poppler-utils (pdf2image dependency)
            subprocess.run(['pdftoppm', '-h'], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("⚠️  pdftoppm not found. Install poppler-utils:")
            print("   macOS: brew install poppler")
            print("   Ubuntu: sudo apt-get install poppler-utils")
            return False
    
    def extract_from_pdf_alternative(self, pdf_path: str, paper_title: str = "") -> List[Dict]:
        """Extract figures using pdf2image approach."""
        if not self.check_dependencies():
            return []
            
        if not os.path.exists(pdf_path):
            print(f"PDF not found: {pdf_path}")
            return []
        
        figures = []
        paper_slug = self.create_slug(paper_title) if paper_title else os.path.splitext(os.path.basename(pdf_path))[0]
        
        print(f"Processing PDF with pdf2image: {os.path.basename(pdf_path)}")
        
        try:
            # Convert PDF pages to images using poppler
            temp_dir = tempfile.mkdtemp()
            
            # Use pdftoppm to convert PDF to images
            cmd = [
                'pdftoppm',
                '-png',
                '-r', '300',  # 300 DPI for good quality
                pdf_path,
                os.path.join(temp_dir, 'page')
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error converting PDF: {result.stderr}")
                return []
            
            # Process converted pages
            page_files = [f for f in os.listdir(temp_dir) if f.startswith('page') and f.endswith('.png')]
            page_files.sort()  # Ensure correct order
            
            for page_file in page_files:
                page_path = os.path.join(temp_dir, page_file)
                page_num = int(page_file.split('-')[1].split('.')[0]) if '-' in page_file else 1
                
                # Extract figures from this page
                page_figures = self.extract_figures_from_page_image(page_path, paper_slug, page_num, paper_title)
                figures.extend(page_figures)
            
            # Cleanup temp directory
            import shutil
            shutil.rmtree(temp_dir)
            
        except Exception as e:
            print(f"Error processing PDF {pdf_path}: {e}")
            return []
        
        print(f"Extracted {len(figures)} figures from {os.path.basename(pdf_path)}")
        return figures
    
    def extract_figures_from_page_image(self, page_path: str, paper_slug: str, page_num: int, paper_title: str) -> List[Dict]:
        """Extract potential figures from a page image by analyzing content."""
        figures = []
        
        try:
            # Load the page image
            page_img = Image.open(page_path)
            
            # Convert to RGB if necessary
            if page_img.mode != 'RGB':
                page_img = page_img.convert('RGB')
            
            # Analyze the page for figure-like regions
            figure_regions = self.detect_figure_regions(page_img)
            
            for i, region in enumerate(figure_regions):
                try:
                    # Extract the region
                    figure_img = page_img.crop(region)
                    
                    # Check if it's a good figure
                    if self.is_good_figure_alternative(figure_img):
                        # Save the figure
                        fig_data = self.save_figure_image(figure_img, paper_slug, page_num, i+1, paper_title)
                        if fig_data:
                            figures.append(fig_data)
                            
                except Exception as e:
                    print(f"Error processing figure region {i} on page {page_num}: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error analyzing page {page_num}: {e}")
            
        return figures
    
    def detect_figure_regions(self, page_img: Image.Image) -> List[Tuple[int, int, int, int]]:
        """Detect potential figure regions in a page image."""
        # Convert to numpy array for analysis
        img_array = np.array(page_img)
        
        # Simple region detection based on content analysis
        # This is a basic implementation - could be improved with more sophisticated methods
        regions = []
        
        width, height = page_img.size
        
        # Divide page into potential figure regions
        # Look for regions that might contain figures (charts, plots, diagrams)
        
        # Top region (abstract/intro figures)
        if height > 400:
            regions.append((0, 0, width, height//3))
        
        # Middle region (main content figures) 
        if height > 600:
            regions.append((0, height//3, width, 2*height//3))
        
        # Bottom region (results/conclusion figures)
        if height > 400:
            regions.append((0, 2*height//3, width, height))
        
        # Full page (for large figures)
        regions.append((0, 0, width, height))
        
        return regions
    
    def is_good_figure_alternative(self, image: Image.Image) -> bool:
        """Determine if an image region is a good figure using alternative criteria."""
        width, height = image.size
        
        # Size checks
        if width < self.min_width or height < self.min_height:
            return False
        
        # Aspect ratio check
        aspect_ratio = width / height
        if aspect_ratio < 0.2 or aspect_ratio > 5.0:  # More permissive for text-heavy figures
            return False
        
        try:
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Calculate image statistics
            stat = ImageStat.Stat(image)
            
            # Check for reasonable color variance (less strict for text figures)
            variance = np.mean(stat.var)
            if variance < 10:  # Very low variance = likely blank
                return False
            
            # Check if it's not just white space
            brightness = np.mean(stat.mean)
            if brightness > 250:  # Almost pure white
                return False
                
        except Exception:
            return False
        
        return True
    
    def save_figure_image(self, figure_img: Image.Image, paper_slug: str, page_num: int, fig_num: int, paper_title: str) -> Dict:
        """Save a figure image and return metadata."""
        try:
            # Create filename
            img_hash = hashlib.md5(figure_img.tobytes()).hexdigest()[:8]
            filename = f"{paper_slug}_page{page_num}_fig{fig_num}_{img_hash}.png"
            filepath = os.path.join(self.figures_dir, filename)
            
            # Save image
            figure_img.save(filepath, "PNG", optimize=True)
            
            figure_info = {
                'filename': filename,
                'filepath': filepath,
                'paper_title': paper_title,
                'paper_slug': paper_slug,
                'page': page_num,
                'size': figure_img.size,
                'file_size': os.path.getsize(filepath),
                'relative_path': f"/images/research/figures/{filename}"
            }
            
            print(f"  Extracted figure: {filename} ({figure_img.size[0]}x{figure_img.size[1]})")
            return figure_info
            
        except Exception as e:
            print(f"Error saving figure: {e}")
            return None
    
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
        
        # Keywords for different categories (order matters - more specific first)
        categories = {
            'foundation-models': ['astromlab', 'llm', 'large language model', 'foundation model', 'gpt', 'language model', 'eaira', 'ai model', 'transformer', 'bert', 'chatgpt'],
            'emulation-inference': ['emulator', 'emulation', 'surrogate', 'power spectrum', 'reduced order', 'interpolation', 'approximation', 'synthetic', 'uncertainty', 'bayesian', 'probabilistic', 'inference', 'mcmc', 'monte carlo'],
            'dark-matter': ['dark matter', 'cosmic web', 'cosmology', 'halo', 'structure formation', 'n-body', 'simulation', 'caustic', 'multistream'],
            'machine-learning': ['machine learning', 'deep learning', 'neural network', 'ai ', 'artificial intelligence', 'model', 'training', 'generative', 'anomaly detection', 'gravitational lens', 'lensing', 'deconvolution'],
            'other-research': []
        }
        
        # Check categories in priority order
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
            'foundation-models': 'portfolio-1-foundation-models.md',
            'machine-learning': 'portfolio-2-machine-learning.md',
            'dark-matter': 'portfolio-3-dark-matter.md', 
            'emulation-inference': 'portfolio-4-emulation-inference.md',
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
        
        # Curate figures for diversity
        curated_figures = self.curate_diverse_figures(figures, max_figures=4, max_per_paper=2)
        
        html = '<div class="research-figures-grid">\n'
        
        for fig in curated_figures:
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
    
    def curate_diverse_figures(self, figures: List[Dict], max_figures: int = 4, max_per_paper: int = 2) -> List[Dict]:
        """Curate figures to show diversity across different papers with randomization."""
        import random
        
        if not figures:
            return []
        
        # Group figures by paper
        papers = {}
        for fig in figures:
            paper_title = fig['paper_title']
            if paper_title not in papers:
                papers[paper_title] = []
            papers[paper_title].append(fig)
        
        # Randomize the order to get variety across runs
        paper_names = list(papers.keys())
        random.shuffle(paper_names)
        
        # Also randomize figures within each paper
        for paper_name in paper_names:
            random.shuffle(papers[paper_name])
        
        # First pass: one figure from each paper that has figures
        curated = []
        for paper_name in paper_names:
            if len(curated) >= max_figures:
                break
            if paper_name not in [fig['paper_title'] for fig in curated] and papers[paper_name]:
                curated.append(papers[paper_name][0])
        
        # Second pass: add more figures from different papers if needed
        for round_num in range(1, max_per_paper):
            for paper_name in paper_names:
                if len(curated) >= max_figures:
                    break
                if round_num < len(papers[paper_name]):
                    # Check if we already have max figures from this paper
                    paper_count = len([fig for fig in curated if fig['paper_title'] == paper_name])
                    if paper_count < max_per_paper:
                        curated.append(papers[paper_name][round_num])
        
        return curated[:max_figures]

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract figures from academic papers using pdf2image')
    parser.add_argument('action', choices=['extract-local', 'extract-url'], 
                       help='Action to perform')
    parser.add_argument('--pdf', help='Path to PDF file (for extract-local)')
    parser.add_argument('--url', help='URL to PDF (for extract-url)')
    parser.add_argument('--title', help='Paper title')
    
    args = parser.parse_args()
    
    extractor = ImprovedFigureExtractor()
    
    if args.action == 'extract-local':
        if not args.pdf:
            print("Error: --pdf is required for extract-local")
            return
        
        figures = extractor.extract_from_pdf_alternative(args.pdf, args.title or "")
        print(f"\nExtracted {len(figures)} figures")
        
    elif args.action == 'extract-url':
        if not args.url:
            print("Error: --url is required for extract-url")
            return
        
        # Download PDF
        pdf_path = extractor.download_pdf_from_url(args.url, args.title or "")
        if pdf_path:
            # Extract figures
            figures = extractor.extract_from_pdf_alternative(pdf_path, args.title or "")
            print(f"\nExtracted {len(figures)} figures")
            
            # Clean up downloaded file
            try:
                os.remove(pdf_path)
            except:
                pass

if __name__ == "__main__":
    main()