#!/usr/bin/env python3
"""
Complete Research Tab Overhaul
===============================
This script completely rebuilds the research page by:
1. Classifying papers into 4 research categories
2. Using Gemini LLM to generate category summaries  
3. Extracting the LAST (best) plot from each paper
4. Creating a clean, professional research page
5. Displaying 2 plots per research category

Run this once to refresh everything.
"""

import os
import sys
import re
import json
import fitz  # PyMuPDF
import requests
import hashlib
from pathlib import Path
from PIL import Image, ImageStat
import numpy as np
import google.generativeai as genai
from typing import Dict, List, Optional
import time

class ResearchOverhaul:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.publications_dir = self.base_dir / "_publications"
        self.research_page = self.base_dir / "_pages" / "research.html"
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.papers_dir = self.base_dir / "temp_papers"
        
        # Create directories
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        self.papers_dir.mkdir(parents=True, exist_ok=True)
        
        # Research categories and their classification keywords
        self.categories = {
            'foundation-models': {
                'name': 'Foundation Models',
                'keywords': [
                    'astromlab', 'eaira', 'llm', 'large language model', 'foundation model',
                    'gpt', 'language model', 'ai model', 'transformer', 'bert', 'chatgpt',
                    'evaluating ai', 'research assistant', 'benchmark'
                ],
                'papers': [],
                'summary': '',
                'plots': []
            },
            'machine-learning': {
                'name': 'Machine Learning for Science',
                'keywords': [
                    'machine learning', 'deep learning', 'neural network', 'ai ', 
                    'artificial intelligence', 'anomaly detection', 'generative',
                    'deconvolution', 'point spread function', 'modular deep learning',
                    'convolutional', 'autoencoder', 'gan', 'variational'
                ],
                'papers': [],
                'summary': '',
                'plots': []
            },
            'dark-matter': {
                'name': 'Dark Matter & Cosmology',
                'keywords': [
                    'dark matter', 'cosmic web', 'cosmology', 'caustic', 'topology',
                    'halo', 'structure formation', 'n-body', 'simulation', 'multistream',
                    'galaxy cluster', 'weak lensing', 'cosmic shear', 'power spectrum'
                ],
                'papers': [],
                'summary': '',
                'plots': []
            },
            'emulation-inference': {
                'name': 'Emulation & Inference',
                'keywords': [
                    'emulator', 'emulation', 'surrogate', 'reduced order', 'probabilistic',
                    'bayesian', 'inference', 'uncertainty quantification', 'monte carlo',
                    'interpolation', 'approximation', 'surrogate model', 'gaussian process'
                ],
                'papers': [],
                'summary': '',
                'plots': []
            }
        }
        
        # Setup Gemini (you'll need to set GEMINI_API_KEY environment variable)
        self.setup_gemini()
    
    def setup_gemini(self):
        """Setup Gemini API for text generation."""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            print("⚠️  GEMINI_API_KEY not found. Set it as environment variable.")
            print("   export GEMINI_API_KEY='your-api-key-here'")
            self.use_gemini = False
        else:
            try:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel('gemini-pro')
                self.use_gemini = True
                print("✅ Gemini API configured successfully")
            except Exception as e:
                print(f"⚠️  Gemini setup failed: {e}")
                self.use_gemini = False
    
    def classify_papers(self):
        """Classify all papers into research categories."""
        print("📚 Classifying papers into research categories...\n")
        
        for pub_file in self.publications_dir.glob("*.md"):
            try:
                with open(pub_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract paper metadata
                title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content, re.MULTILINE | re.DOTALL)
                title = title_match.group(1) if title_match else pub_file.stem
                
                # Get paper URL for downloading
                paper_url = self.extract_paper_url(content)
                
                # Extract publication year
                year_match = re.search(r'date:\s*(\d{4})', content)
                year = int(year_match.group(1)) if year_match else 2020
                
                paper_info = {
                    'title': title,
                    'file': pub_file.name,
                    'url': paper_url,
                    'year': year,
                    'content': content
                }
                
                # Classify into category
                category = self.classify_paper(title, content)
                if category:
                    self.categories[category]['papers'].append(paper_info)
                    print(f"✅ {category}: {title[:60]}{'...' if len(title) > 60 else ''}")
                
            except Exception as e:
                print(f"⚠️ Error processing {pub_file.name}: {e}")
        
        # Print classification summary
        print(f"\n📊 Classification Summary:")
        for cat_key, cat_info in self.categories.items():
            print(f"   {cat_info['name']}: {len(cat_info['papers'])} papers")
    
    def extract_paper_url(self, content: str) -> Optional[str]:
        """Extract downloadable PDF URL from paper content."""
        # Check for arXiv URLs in different fields
        patterns = [
            r'paperurl:\s*["\']?([^"\'\\s]+arxiv[^"\'\\s]*)["\']?',
            r'arxiv\.org/abs/([^)\\s]+)',
            r'arxiv\.org/pdf/([^)\\s]+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if 'arxiv.org' in match:
                    # Convert to PDF URL
                    if '/abs/' in match:
                        return match.replace('/abs/', '/pdf/') + '.pdf'
                    elif '/pdf/' in match and not match.endswith('.pdf'):
                        return match + '.pdf'
                    elif '/pdf/' in match and match.endswith('.pdf'):
                        return match
                    else:
                        return f"https://arxiv.org/pdf/{match}.pdf"
        
        return None
    
    def classify_paper(self, title: str, content: str) -> Optional[str]:
        """Classify a paper into one of the research categories."""
        text = (title + ' ' + content).lower()
        
        # Score each category
        scores = {}
        for cat_key, cat_info in self.categories.items():
            score = 0
            for keyword in cat_info['keywords']:
                if keyword.lower() in text:
                    score += 1
            scores[cat_key] = score
        
        # Return category with highest score (if > 0)
        if max(scores.values()) > 0:
            return max(scores, key=scores.get)
        
        return None
    
    def download_papers(self):
        """Download papers that don't exist locally."""
        print("\n📥 Downloading papers...")
        
        for cat_key, cat_info in self.categories.items():
            for paper in cat_info['papers']:
                if not paper['url']:
                    continue
                
                # Create safe filename
                safe_title = re.sub(r'[^\w\s-]', '', paper['title'])
                safe_title = re.sub(r'\s+', '_', safe_title)
                filename = f"{safe_title[:50]}.pdf"
                filepath = self.papers_dir / filename
                
                if filepath.exists():
                    print(f"   ✅ Already have: {filename}")
                    paper['local_path'] = str(filepath)
                    continue
                
                try:
                    print(f"   📥 Downloading: {paper['title'][:50]}...")
                    
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                    }
                    
                    response = requests.get(paper['url'], headers=headers, stream=True, timeout=60)
                    response.raise_for_status()
                    
                    with open(filepath, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    
                    paper['local_path'] = str(filepath)
                    print(f"      ✅ Saved: {filename}")
                    time.sleep(2)  # Be nice to servers
                    
                except Exception as e:
                    print(f"      ❌ Failed: {e}")
                    paper['local_path'] = None
    
    def extract_last_plot_from_paper(self, pdf_path: str, paper_title: str) -> Optional[Dict]:
        """Extract the LAST (best) plot from a paper."""
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"      ❌ Error opening PDF: {e}")
            return None
        
        print(f"   🔍 Extracting last plot from: {paper_title[:40]}...")
        
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
                    
                    # Quality checks for scientific figures
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
                        
                        all_figures.append({
                            'image': image,
                            'image_bytes': image_bytes,
                            'hash': img_hash[:8],
                            'size': image.size,
                            'quality_score': quality_score,
                            'page': page_num + 1,
                            'position_score': page_num  # Later pages = higher score
                        })
                        
                except Exception as e:
                    continue
        
        doc.close()
        
        if not all_figures:
            print(f"      ❌ No suitable figures found")
            return None
        
        # Select the LAST figure (highest page number) that also has good quality
        # Sort by page number (descending) then by quality score (descending)
        all_figures.sort(key=lambda x: (x['position_score'], x['quality_score']), reverse=True)
        best_figure = all_figures[0]
        
        # Save the figure
        safe_title = re.sub(r'[^\w\s-]', '', paper_title)
        safe_title = re.sub(r'\s+', '_', safe_title)
        filename = f"{safe_title[:40]}_last_plot_{best_figure['hash']}.png"
        filepath = self.figures_dir / filename
        
        if best_figure['image'].mode != 'RGB':
            best_figure['image'] = best_figure['image'].convert('RGB')
        best_figure['image'].save(filepath, "PNG", optimize=True)
        
        plot_info = {
            'filename': filename,
            'paper_title': paper_title,
            'size': best_figure['size'],
            'page': best_figure['page'],
            'relative_path': f"/images/research/figures/{filename}",
            'quality_score': best_figure['quality_score']
        }
        
        print(f"      ✅ Extracted last plot: {filename} (page {best_figure['page']}, {best_figure['size'][0]}x{best_figure['size'][1]})")
        return plot_info
    
    def is_good_scientific_figure(self, image: Image.Image, file_size: int) -> bool:
        """Check if image is a good scientific figure."""
        width, height = image.size
        
        # Size requirements
        if width < 300 or height < 200 or file_size < 15000:
            return False
        
        # Aspect ratio
        aspect_ratio = width / height
        if aspect_ratio < 0.3 or aspect_ratio > 4.0:
            return False
        
        try:
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            stat = ImageStat.Stat(image)
            variance = np.mean(stat.var)
            
            # Scientific figures should have reasonable complexity
            if variance < 80:
                return False
                
        except Exception:
            return False
        
        return True
    
    def extract_plots_for_categories(self):
        """Extract the last plot from each paper in each category."""
        print("\n🎨 Extracting last plots from papers...")
        
        for cat_key, cat_info in self.categories.items():
            print(f"\n📊 Processing {cat_info['name']} papers:")
            
            for paper in cat_info['papers']:
                if not paper.get('local_path') or not os.path.exists(paper['local_path']):
                    print(f"   ⚠️ Skipping {paper['title'][:40]} - no local PDF")
                    continue
                
                plot = self.extract_last_plot_from_paper(paper['local_path'], paper['title'])
                if plot:
                    cat_info['plots'].append(plot)
            
            print(f"   📈 Total plots for {cat_info['name']}: {len(cat_info['plots'])}")
    
    def generate_category_summaries(self):
        """Generate LLM summaries for each research category."""
        print("\n🤖 Generating research category summaries with Gemini...")
        
        for cat_key, cat_info in self.categories.items():
            if not cat_info['papers']:
                cat_info['summary'] = f"Research in {cat_info['name']} is ongoing with several publications in development."
                continue
            
            # Prepare paper titles for LLM
            paper_titles = [paper['title'] for paper in cat_info['papers']]
            
            if self.use_gemini:
                prompt = f"""
You are a research scientist writing a summary of research work in {cat_info['name']}. 
Based on the following paper titles from Dr. Nesar Ramachandra's research, write a 2-3 paragraph summary describing the research contributions and impact in this area.

Paper titles:
{chr(10).join('- ' + title for title in paper_titles)}

Write a professional, technical summary that highlights the key contributions, methodologies, and impact of this research. Focus on the scientific advances and their significance to the field. Keep it to 2-3 paragraphs, around 150-200 words total.
"""
                
                try:
                    response = self.model.generate_content(prompt)
                    cat_info['summary'] = response.text.strip()
                    print(f"   ✅ Generated summary for {cat_info['name']}")
                    time.sleep(1)  # Rate limiting
                    
                except Exception as e:
                    print(f"   ❌ Failed to generate summary for {cat_info['name']}: {e}")
                    cat_info['summary'] = self.generate_fallback_summary(cat_info['name'], paper_titles)
            else:
                cat_info['summary'] = self.generate_fallback_summary(cat_info['name'], paper_titles)
    
    def generate_fallback_summary(self, category_name: str, paper_titles: List[str]) -> str:
        """Generate a fallback summary when LLM is not available."""
        num_papers = len(paper_titles)
        
        summaries = {
            'Foundation Models': f"Research in foundation models focuses on developing specialized AI systems for scientific applications. This work includes {num_papers} publications exploring large language models, evaluation methodologies, and domain-specific AI assistants. The research contributes to advancing AI capabilities for scientific research and education, with particular emphasis on astronomy and astrophysics applications.",
            
            'Machine Learning for Science': f"This research area encompasses {num_papers} publications applying machine learning techniques to scientific problems. The work includes developing neural networks for astronomical data analysis, implementing generative models for scientific applications, and creating advanced algorithms for pattern recognition and anomaly detection. These contributions advance the integration of AI methodologies in scientific research workflows.",
            
            'Dark Matter & Cosmology': f"Research in dark matter and cosmology involves {num_papers} publications investigating large-scale structure formation and cosmic web analysis. This work contributes to understanding dark matter distribution, cosmic structure evolution, and gravitational effects on cosmic scales. The research combines theoretical modeling with observational data analysis to advance our understanding of the universe's fundamental structure.",
            
            'Emulation & Inference': f"This research area includes {num_papers} publications developing statistical emulators and inference methods for scientific applications. The work focuses on surrogate modeling, uncertainty quantification, and probabilistic inference techniques. These contributions enable efficient analysis of complex scientific models and provide robust uncertainty estimates for scientific predictions."
        }
        
        return summaries.get(category_name, f"Research in {category_name} includes {num_papers} publications contributing to advancing scientific understanding and methodology in this important field.")
    
    def create_research_page(self):
        """Create a completely new research page with proper layout."""
        print("\n🎨 Creating new research page...")
        
        html_content = self.generate_research_html()
        
        with open(self.research_page, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Research page created: {self.research_page}")
    
    def generate_research_html(self) -> str:
        """Generate the complete HTML for the research page."""
        
        # Generate sections for each category
        sections_html = ""
        
        colors = {
            'foundation-models': '#6366f1',
            'machine-learning': '#3b82f6', 
            'dark-matter': '#8b5cf6',
            'emulation-inference': '#f59e0b'
        }
        
        for cat_key, cat_info in self.categories.items():
            # Select top 2 plots for display
            display_plots = sorted(cat_info['plots'], key=lambda x: x['quality_score'], reverse=True)[:2]
            
            # Generate plots HTML
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
            
            # Create portfolio link
            portfolio_link = f"/portfolio/portfolio-{list(self.categories.keys()).index(cat_key) + 1}-{cat_key.replace('_', '-')}/"
            
            section_html = f'''
    <div class="research-section" style="border-left: 4px solid {colors[cat_key]};">
      <div class="research-header">
        <h2>
          <a href="{portfolio_link}" class="research-title">{cat_info['name']}</a>
        </h2>
        <div class="research-summary">
          {cat_info['summary']}
        </div>
      </div>
      
      <div class="research-figures">
{plots_html}      </div>
      
      <div class="research-stats">
        <span class="stat">{len(cat_info['papers'])} Publications</span>
        <span class="stat">{len(cat_info['plots'])} Figures Available</span>
      </div>
    </div>
'''
            sections_html += section_html
        
        # Complete HTML template
        html_template = f"""---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<div class="research-overview">
  <div class="research-intro">
    <p>My research focuses on developing and applying computational methods at the intersection of astrophysics, cosmology, and machine learning. The work spans foundation models for scientific applications, advanced ML techniques for astronomical data analysis, cosmic structure investigation, and statistical inference methods.</p>
  </div>

  <div class="research-content">
{sections_html}  </div>
</div>

<!-- Figure Modal -->
<div id="imageModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="modalImage">
</div>

<style>
.research-overview {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}}

.research-intro {{
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}}

.research-intro p {{
  font-size: 1.1em;
  line-height: 1.7;
  color: #4a5568;
  max-width: 800px;
  margin: 0 auto;
}}

.research-content {{
  display: flex;
  flex-direction: column;
  gap: 3rem;
}}

.research-section {{
  background: white;
  border-radius: 12px;
  padding: 2.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.research-section:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
}}

.research-header {{
  margin-bottom: 2rem;
}}

.research-header h2 {{
  font-size: 1.8em;
  font-weight: 700;
  margin-bottom: 1rem;
}}

.research-title {{
  color: #2d3748;
  text-decoration: none;
  transition: color 0.2s ease;
}}

.research-title:hover {{
  color: #3182ce;
}}

.research-summary {{
  font-size: 1.05em;
  line-height: 1.7;
  color: #4a5568;
  text-align: justify;
}}

.research-figures {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}}

.research-figure {{
  text-align: center;
  background: #f8f9fa;
  border-radius: 12px;
  padding: 1.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.research-figure:hover {{
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}}

.research-figure img {{
  max-width: 100%;
  height: auto;
  max-height: 300px;
  object-fit: contain;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}}

.research-figure img:hover {{
  opacity: 0.9;
}}

.figure-caption {{
  font-size: 0.9em;
  color: #6c757d;
  margin-top: 1rem;
  line-height: 1.4;
  font-style: italic;
}}

.no-figures {{
  grid-column: 1 / -1;
  text-align: center;
  padding: 3rem;
  color: #718096;
  font-style: italic;
  background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
  border-radius: 12px;
  border: 2px dashed #cbd5e0;
}}

.research-stats {{
  display: flex;
  gap: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #e2e8f0;
}}

.stat {{
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #edf2f7 0%, #e2e8f0 100%);
  border-radius: 20px;
  font-size: 0.9em;
  font-weight: 600;
  color: #4a5568;
}}

/* Modal styles */
.modal {{
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
}}

.modal-content {{
  margin: auto;
  display: block;
  width: 90%;
  max-width: 1000px;
  max-height: 90vh;
  object-fit: contain;
  margin-top: 2%;
}}

.close {{
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.3s ease;
}}

.close:hover {{
  color: #bbb;
}}

/* Responsive design */
@media (max-width: 768px) {{
  .research-overview {{
    padding: 0 0.5rem;
  }}
  
  .research-section {{
    padding: 1.5rem;
  }}
  
  .research-figures {{
    grid-template-columns: 1fr;
    gap: 1rem;
  }}
  
  .research-stats {{
    flex-direction: column;
    gap: 1rem;
  }}
  
  .modal-content {{
    width: 95%;
    margin-top: 5%;
  }}
}}
</style>

<script>
function openModal(img) {{
  var modal = document.getElementById('imageModal');
  var modalImg = document.getElementById('modalImage');
  modal.style.display = 'block';
  modalImg.src = img.src;
}}

function closeModal() {{
  document.getElementById('imageModal').style.display = 'none';
}}

// Close modal when clicking outside the image
window.onclick = function(event) {{
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {{
    modal.style.display = 'none';
  }}
}}

// Close modal with escape key
document.addEventListener('keydown', function(event) {{
  if (event.key === 'Escape') {{
    closeModal();
  }}
}});
</script>
"""
        
        return html_template
    
    def run_complete_overhaul(self):
        """Run the complete research overhaul process."""
        print("🚀 Starting Complete Research Tab Overhaul...\n")
        print("=" * 60)
        
        # Step 1: Classify papers
        self.classify_papers()
        
        # Step 2: Download papers
        self.download_papers()
        
        # Step 3: Extract plots (last plot from each paper)
        self.extract_plots_for_categories()
        
        # Step 4: Generate LLM summaries
        self.generate_category_summaries()
        
        # Step 5: Create new research page
        self.create_research_page()
        
        # Final summary
        print("\n" + "=" * 60)
        print("🎉 RESEARCH OVERHAUL COMPLETE!")
        print("=" * 60)
        
        total_papers = sum(len(cat['papers']) for cat in self.categories.values())
        total_plots = sum(len(cat['plots']) for cat in self.categories.values())
        
        print(f"\n📊 Final Summary:")
        print(f"   📚 Total papers classified: {total_papers}")
        print(f"   🎨 Total plots extracted: {total_plots}")
        print(f"   🤖 LLM summaries: {'✅ Generated' if self.use_gemini else '✅ Fallback used'}")
        print(f"   🎨 Research page: ✅ Completely rebuilt")
        
        print(f"\n📋 By Category:")
        for cat_key, cat_info in self.categories.items():
            print(f"   {cat_info['name']}: {len(cat_info['papers'])} papers, {len(cat_info['plots'])} plots")
        
        print(f"\n✨ The research page has been completely overhauled with:")
        print(f"   • Professional, clean interface")
        print(f"   • LLM-generated research summaries")  
        print(f"   • Last (best) plots from each paper")
        print(f"   • 2 plots displayed per research category")
        print(f"   • Responsive design with modal viewing")

def main():
    """Main function to run the research overhaul."""
    overhaul = ResearchOverhaul()
    overhaul.run_complete_overhaul()

if __name__ == "__main__":
    main()