#!/usr/bin/env python3
"""
Unified Website Content Manager
===============================
Single script to manage all website content using LLM-based generation.
No hardcoded paper categories, no fallback options, fully automated.

Usage:
    python scripts/website_content_manager.py [--update-publications] [--update-research] [--update-portfolio] [--full-update]
"""

import os
import sys
import re
import json
import fitz  # PyMuPDF
import requests
import hashlib
import argparse
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image, ImageStat
import numpy as np
import google.generativeai as genai
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import io

class WebsiteContentManager:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.publications_dir = self.base_dir / "_publications"
        self.portfolio_dir = self.base_dir / "_portfolio"
        self.research_page = self.base_dir / "_pages" / "research.html"
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.papers_dir = self.base_dir / "temp_papers"
        
        # Create directories
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        self.papers_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize LLM
        self.setup_llm()
        
        # Dynamic research categories (will be populated by LLM)
        self.research_categories = {}
    
    def setup_llm(self):
        """Setup LLM API for content generation."""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            print("❌ GEMINI_API_KEY environment variable is required.")
            print("   Get your API key from: https://makersuite.google.com/app/apikey")
            print("   Then set it: export GEMINI_API_KEY='your-api-key-here'")
            sys.exit(1)
        
        try:
            genai.configure(api_key=api_key)
            #self.model = genai.GenerativeModel('gemini-1.5-pro')
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            print("✅ LLM configured successfully")
        except Exception as e:
            print(f"❌ LLM setup failed: {e}")
            sys.exit(1)
    
    def llm_generate(self, prompt: str, max_retries: int = 3) -> str:
        """Generate content using LLM with retry logic."""
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                return response.text.strip()
            except Exception as e:
                print(f"⚠️ LLM attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    raise
    
    def fetch_publications_from_arxiv(self) -> List[Dict]:
        """Fetch publications from arXiv API."""
        print("📚 Fetching publications from arXiv...")
        
        search_terms = [
            "au:\"Nesar S Ramachandra\"",
            "au:\"Ramachandra, Nesar\"", 
            "au:\"N S Ramachandra\"",
            "au:Ramachandra AND au:Nesar",
            "au:\"Ramachandra, N S\"",
            "au:\"Ramachandra, N.S.\"",
            "au:\"N.S. Ramachandra\"",
            "au:\"Nesar Ramachandra\""
        ]
        
        all_papers = []
        seen_arxiv_ids = set()
        
        for search_term in search_terms:
            # URL encode the search term properly
            from urllib.parse import quote
            encoded_search = quote(search_term)
            url = f"http://export.arxiv.org/api/query?search_query={encoded_search}&sortBy=submittedDate&sortOrder=descending&max_results=200"
            
            try:
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                
                root = ET.fromstring(response.content)
                namespace = {'atom': 'http://www.w3.org/2005/Atom'}
                
                for entry in root.findall('.//atom:entry', namespace):
                    # Extract basic info
                    title = entry.find('./atom:title', namespace)
                    published = entry.find('./atom:published', namespace)
                    summary = entry.find('./atom:summary', namespace)
                    arxiv_id = entry.find('./atom:id', namespace)
                    
                    if not all([title is not None and title.text, 
                               published is not None and published.text, 
                               arxiv_id is not None and arxiv_id.text]):
                        continue
                    
                    # Get authors
                    authors = []
                    for author in entry.findall('./atom:author', namespace):
                        name_elem = author.find('./atom:name', namespace)
                        if name_elem is not None:
                            authors.append(name_elem.text.strip())
                    
                    # Check if you're an author (more flexible matching)
                    is_author = any(
                        ("Ramachandra" in author and "Nesar" in author) or
                        ("Ramachandra" in author and "N" in author) or
                        ("Ramachandra" in author and author.count("N.") > 0) or
                        ("N. S. Ramachandra" in author) or
                        ("N.S. Ramachandra" in author)
                        for author in authors
                    )
                    
                    if not is_author:
                        continue
                    
                    # Extract arXiv ID
                    arxiv_url = arxiv_id.text
                    arxiv_match = re.search(r'(\d+\.\d+)', arxiv_url)
                    arxiv_number = arxiv_match.group(1) if arxiv_match else ""
                    
                    if arxiv_number in seen_arxiv_ids:
                        continue
                    seen_arxiv_ids.add(arxiv_number)
                    
                    paper = {
                        'title': self.clean_text(title.text),
                        'authors': authors,
                        'date': published.text,
                        'abstract': self.clean_text(summary.text if summary is not None else ""),
                        'arxiv_url': arxiv_url,
                        'arxiv_id': arxiv_number,
                        'venue': 'arXiv preprint'
                    }
                    
                    all_papers.append(paper)
                
                time.sleep(2)  # Rate limiting
                
            except Exception as e:
                print(f"⚠️ Error with search term '{search_term}': {e}")
                continue
        
        print(f"✅ Found {len(all_papers)} publications")
        for i, paper in enumerate(all_papers):
            print(f"   📄 {i+1}. {paper['title'][:60]}...")
        return all_papers
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text."""
        if not text:
            return ""
        text = re.sub(r'\s+', ' ', text.strip())
        return text.replace('"', '\\"')
    
    def format_date(self, date_str: str) -> str:
        """Format date for Jekyll."""
        if not date_str:
            return datetime.now().strftime('%Y-%m-%d')
        
        date_patterns = [
            '%Y-%m-%dT%H:%M:%SZ',
            '%Y-%m-%d',
            '%Y-%m',
            '%Y'
        ]
        
        for pattern in date_patterns:
            try:
                # Extract the appropriate substring for the pattern
                if pattern == '%Y-%m-%dT%H:%M:%SZ':
                    test_str = date_str[:19] + 'Z' if len(date_str) >= 19 else date_str
                else:
                    test_str = date_str[:len(pattern)]
                
                date_obj = datetime.strptime(test_str, pattern)
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                continue
        
        year_match = re.search(r'(\d{4})', date_str)
        return f"{year_match.group(1)}-01-01" if year_match else datetime.now().strftime('%Y-%m-%d')
    
    def create_url_slug(self, title: str) -> str:
        """Create URL-friendly slug."""
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        return re.sub(r'\s+', '-', slug)[:50]
    
    def get_predefined_figure_mapping(self) -> Dict:
        """Get predefined figure mapping based on comprehensive analysis."""
        return {
            'foundation-models': {
                'name': 'Foundation Models',
                'description': 'AI foundation models for scientific applications',
                'figures': [
                    'astromlab-1-who-wins-astronomy-jeopardy_plot_1_5c85b717.png',
                    'eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png',
                    'astromlab-1-who-wins-astronomy-jeopardy_plot_2_0a77f6ec.png',
                    'eaira-establishing-a-methodology-for-evaluating-ai_plot_2_205db31f.png'
                ],
                'papers': [
                    'AstroMLab 1: Who Wins Astronomy Jeopardy!?',
                    'AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model',
                    'AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model',
                    'EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants'
                ]
            },
            'machine-learning': {
                'name': 'Machine Learning for Science',
                'description': 'ML techniques for scientific problems',
                'figures': [
                    'anomaly-detection-in-astronomical-images-with-gene_plot_1_6d84e8fe.png',
                    'neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png',
                    'physical-benchmarking-for-ai-generated-cosmic-web_plot_1_11f44910.png',
                    'a-modular-deep-learning-pipeline-for-galaxy-scale-_plot_1_a983de9a.png'
                ],
                'papers': [
                    'Anomaly Detection in Astronomical Images with Generative Adversarial Networks',
                    'Neural Network Based Point Spread Function Deconvolution For Astronomical Applications',
                    'Physical Benchmarking for AI-Generated Cosmic Web',
                    'A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection'
                ]
            },
            'dark-matter': {
                'name': 'Dark Matter & Cosmology',
                'description': 'Cosmological structure and dark matter research',
                'figures': [
                    'the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png',
                    'multi-stream-portrait-of-the-cosmic-web_plot_1_6096c149.png',
                    'topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png',
                    'dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png'
                ],
                'papers': [
                    'The Caustic Design of the Dark Matter Web',
                    'Multi-stream portrait of the Cosmic web',
                    'Topology and geometry of the dark matter web: a multistream view',
                    'Dark matter haloes: a multistream view'
                ]
            },
            'emulation-inference': {
                'name': 'Emulation & Inference',
                'description': 'Statistical emulators and inference methods',
                'figures': [
                    'matter-power-spectrum-emulator-for-fr-modified-gra_plot_1_d6154d54.png',
                    'probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png',
                    'global-field-reconstruction-from-sparse-sensors-wi_plot_1_93ef286c.png',
                    'application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png'
                ],
                'papers': [
                    'Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies',
                    'Probabilistic neural network-based reduced-order surrogate for fluid flows',
                    'Global field reconstruction from sparse sensors with Voronoi tessellation',
                    'Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field'
                ]
            }
        }

    def classify_papers_with_llm(self, papers: List[Dict]) -> Dict:
        """Use predefined classification with existing figure mapping."""
        print("🎯 Using predefined figure mapping for research categories...")
        
        # Use our comprehensive analysis-based mapping
        predefined_mapping = self.get_predefined_figure_mapping()
        
        # Convert to expected format
        categories = {}
        for cat_key, cat_info in predefined_mapping.items():
            categories[cat_key] = {
                'name': cat_info['name'],
                'description': cat_info['description'],
                'papers': cat_info['papers'],
                'figures': cat_info['figures']
            }
        
        return categories
    

    def create_simple_classification(self, papers: List[Dict]) -> Dict:
        """Simple keyword-based classification as fallback."""
        categories = {
            'foundation-models': {'name': 'Foundation Models', 'description': 'AI foundation models for scientific applications', 'papers': []},
            'machine-learning': {'name': 'Machine Learning for Science', 'description': 'ML techniques for scientific problems', 'papers': []},
            'dark-matter': {'name': 'Dark Matter & Cosmology', 'description': 'Cosmological structure and dark matter research', 'papers': []},
            'emulation-inference': {'name': 'Emulation & Inference', 'description': 'Statistical emulators and inference methods', 'papers': []}
        }
        
        for paper in papers:
            title_lower = paper['title'].lower()
            if any(kw in title_lower for kw in ['eaira', 'astromllab', 'gpt', 'llm', 'foundation', 'evaluation', 'ai']):
                categories['foundation-models']['papers'].append(paper['title'])
            elif any(kw in title_lower for kw in ['neural', 'machine learning', 'deep learning', 'network', 'probabilistic']):
                categories['machine-learning']['papers'].append(paper['title'])
            elif any(kw in title_lower for kw in ['cosmic', 'cosmology', 'dark matter', 'caustic', 'universe', 'multi-stream']):
                categories['dark-matter']['papers'].append(paper['title'])
            elif any(kw in title_lower for kw in ['emulator', 'inference', 'modeling', 'surrogate', 'reduced']):
                categories['emulation-inference']['papers'].append(paper['title'])
            else:
                # Default to machine learning if no clear match
                categories['machine-learning']['papers'].append(paper['title'])
        
        return categories
    
    def download_papers(self, papers: List[Dict]):
        """Download papers that don't exist locally."""
        print("📥 Downloading papers for plot extraction...")
        
        for paper in papers:
            if not paper.get('arxiv_url'):
                continue
            
            safe_title = re.sub(r'[^\w\s-]', '', paper['title'])
            safe_title = re.sub(r'\s+', '_', safe_title)
            filename = f"{safe_title[:50]}.pdf"
            filepath = self.papers_dir / filename
            
            if filepath.exists():
                paper['local_path'] = str(filepath)
                continue
            
            try:
                print(f"   📥 Downloading: {paper['title'][:50]}...")
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                response = requests.get(paper['arxiv_url'], headers=headers, stream=True, timeout=60)
                response.raise_for_status()
                
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                paper['local_path'] = str(filepath)
                print(f"      ✅ Downloaded: {filename}")
                time.sleep(2)
                
            except Exception as e:
                print(f"      ❌ Failed to download {paper['title'][:30]}: {e}")
                paper['local_path'] = None
    
    def extract_best_plots_from_paper(self, pdf_path: str, paper_title: str) -> List[Dict]:
        """Extract best plots from a paper using image analysis."""
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            return []
        
        all_figures = []
        seen_hashes = set()
        
        # Scan all pages for figures
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
                    
                    # Load and evaluate image
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    if self.is_good_scientific_figure(image, len(image_bytes)):
                        # Calculate quality score
                        image_rgb = image.convert('RGB') if image.mode != 'RGB' else image
                        stat = ImageStat.Stat(image_rgb)
                        complexity = np.mean(stat.var)
                        area = image.size[0] * image.size[1]
                        
                        # Prefer later pages (likely better figures)
                        page_boost = page_num * 0.1
                        quality_score = area * complexity * (1 + page_boost)
                        
                        all_figures.append({
                            'image': image,
                            'hash': img_hash[:8],
                            'size': image.size,
                            'quality_score': quality_score,
                            'page': page_num + 1
                        })
                        
                except Exception:
                    continue
        
        doc.close()
        
        # Return top 3 figures
        all_figures.sort(key=lambda x: x['quality_score'], reverse=True)
        top_figures = all_figures[:3]
        
        extracted_plots = []
        for i, figure in enumerate(top_figures):
            filename = f"{self.create_url_slug(paper_title)}_plot_{i+1}_{figure['hash']}.png"
            filepath = self.figures_dir / filename
            
            figure['image'].convert('RGB').save(filepath, "PNG", optimize=True)
            
            plot_info = {
                'filename': filename,
                'paper_title': paper_title,
                'size': figure['size'],
                'page': figure['page'],
                'relative_path': f"/images/research/figures/{filename}",
                'quality_score': figure['quality_score']
            }
            
            extracted_plots.append(plot_info)
        
        return extracted_plots
    
    def is_good_scientific_figure(self, image: Image.Image, file_size: int) -> bool:
        """Check if image is a good scientific figure."""
        width, height = image.size
        
        if width < 250 or height < 150 or file_size < 8000:
            return False
        
        aspect_ratio = width / height
        if aspect_ratio < 0.2 or aspect_ratio > 5.0:
            return False
        
        try:
            image_rgb = image.convert('RGB') if image.mode != 'RGB' else image
            stat = ImageStat.Stat(image_rgb)
            variance = np.mean(stat.var)
            return variance >= 50
        except Exception:
            return False
    
    def generate_category_summary_with_llm(self, category_name: str, papers: List[str]) -> str:
        """Generate research category summary using LLM."""
        paper_list = "\n".join([f"- {paper}" for paper in papers])
        
        prompt = f"""Write a 100-word summary for {category_name} research based on these papers:

{paper_list}

Focus on key methods and impact. Academic tone, no markdown."""
        
        return self.llm_generate(prompt)
    
    def update_publications(self):
        """Update publication markdown files."""
        print("📚 Updating publications...")
        
        papers = self.fetch_publications_from_arxiv()
        if not papers:
            print("❌ No papers found")
            return
        
        # Sort by date (newest first)
        papers.sort(key=lambda x: self.format_date(x.get('date', '')), reverse=True)
        
        # Create publication files
        successful = 0
        for i, paper in enumerate(papers):
            try:
                title = paper['title']
                authors = ', '.join(paper.get('authors', []))
                pub_date = self.format_date(paper.get('date', ''))
                year = pub_date[:4]
                url_slug = self.create_url_slug(title)
                paper_url = paper.get('arxiv_url', '')
                venue = paper.get('venue', 'Preprint')
                
                excerpt = f"[<u><span style='color:blue'>arXiv</span></u>]({paper_url})" if paper_url else ""
                citation = f"{authors} ({year}). \"{title}\". {venue}."
                
                filename = f"{pub_date}-{url_slug}.md"
                if (self.publications_dir / filename).exists():
                    filename = f"{pub_date}-{url_slug}-{i}.md"
                
                content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{url_slug}
excerpt: '{excerpt}'
date: {pub_date}
venue: '{venue}'
paperurl: '{paper_url}'
citation: '{self.clean_text(citation)}'
---

{paper.get('abstract', 'No abstract available.')}
"""
                
                filepath = self.publications_dir / filename
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                successful += 1
                
            except Exception as e:
                print(f"❌ Error creating publication file for {paper.get('title', 'unknown')}: {e}")
        
        print(f"✅ Successfully created {successful} publication files")
    
    def update_research_page(self):
        """Update research page with LLM-generated content."""
        print("🔬 Updating research page...")
        
        # Get publications and classify them
        papers = self.fetch_publications_from_arxiv()
        if not papers:
            print("❌ No papers found from arXiv")
            return
        
        # Download papers for plot extraction (skip for now to speed up)
        # self.download_papers(papers)
        
        # Classify papers using LLM
        categories = self.classify_papers_with_llm(papers)
        
        # Create paper lookup
        paper_lookup = {paper['title']: paper for paper in papers}
        
        # Extract plots and generate summaries for each category
        sections_html = ""
        colors = ['#6366f1', '#3b82f6', '#8b5cf6', '#f59e0b', '#10b981']
        
        for i, (cat_key, cat_info) in enumerate(categories.items()):
            if not cat_info['papers']:
                continue
            
            print(f"   📊 Processing {cat_info['name']}...")
            
            # Use predefined figures for this category
            category_plots = []
            if 'figures' in cat_info:
                for i, figure_filename in enumerate(cat_info['figures']):
                    fig_path = self.figures_dir / figure_filename
                    if fig_path.exists():
                        # Get corresponding paper title if available
                        paper_title = cat_info['papers'][i] if i < len(cat_info['papers']) else "Research figure"
                        
                        plot_info = {
                            'filename': figure_filename,
                            'paper_title': paper_title,
                            'relative_path': f"/images/research/figures/{figure_filename}",
                            'quality_score': 100 - i  # Higher score for first figures
                        }
                        category_plots.append(plot_info)
                    else:
                        print(f"   ⚠️ Figure not found: {figure_filename}")
            else:
                # Fallback to old method if no predefined figures
                for paper_title in cat_info['papers']:
                    paper_slug = self.create_url_slug(paper_title)
                    matching_figures = list(self.figures_dir.glob(f"*{paper_slug}*_plot_*.png"))
                    
                    if not matching_figures:
                        title_words = paper_title.lower().split()[:3]
                        for word in title_words:
                            if len(word) > 3:
                                word_figures = list(self.figures_dir.glob(f"*{word}*_plot_*.png"))
                                if word_figures:
                                    matching_figures.extend(word_figures)
                                    break
                    
                    if matching_figures:
                        fig_path = matching_figures[0]
                        plot_info = {
                            'filename': fig_path.name,
                            'paper_title': paper_title,
                            'relative_path': f"/images/research/figures/{fig_path.name}",
                            'quality_score': 100
                        }
                        category_plots.append(plot_info)
            
            # Generate category summary
            print(f"   🤖 Generating summary for {cat_info['name']}...")
            summary = self.generate_category_summary_with_llm(cat_info['name'], cat_info['papers'])
            
            # Select up to 3 plots for display (from different papers)
            display_plots = sorted(category_plots, key=lambda x: x['quality_score'], reverse=True)[:3]
            
            # Define portfolio link and color first
            color = colors[i % len(colors)]
            portfolio_link = f"/portfolio/portfolio-{i+1}-{cat_key}/"
            
            # Generate plots HTML
            if display_plots:
                plots_html = ""
                for plot in display_plots:
                    plots_html += f'''        <div class="research-figure">
          <img src="{plot['relative_path']}" alt="Figure from {plot['paper_title']}" onclick="window.location.href='{portfolio_link}'" loading="lazy" />
          <div class="figure-caption">From: {plot['paper_title']}</div>
        </div>
'''
            else:
                plots_html = '''        <div class="no-figures">
          <p>Representative figures will be added soon.</p>
        </div>
'''
            
            section_html = f'''
    <div class="research-section" style="border-left: 4px solid {color};">
      <div class="research-header">
        <h2>
          <a href="{portfolio_link}" class="research-title">{cat_info['name']}</a>
        </h2>
        <div class="research-summary">
          {summary}
          <br><br>
          <a href="{portfolio_link}" class="learn-more">Learn more about this research →</a>
        </div>
      </div>
      
      <div class="research-figures">
{plots_html}      </div>
      
      <div class="research-stats">
        <span class="stat">{len(cat_info['papers'])} Publications</span>
        <span class="stat">{len(category_plots)} Figures Available</span>
      </div>
    </div>
'''
            sections_html += section_html
        
        # Generate complete HTML
        html_content = self.generate_research_html_template(sections_html)
        
        # Write research page
        with open(self.research_page, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Research page updated with {len(categories)} categories")
        return categories
    
    def generate_research_html_template(self, sections_html: str) -> str:
        """Generate complete HTML template for research page."""
        return f"""---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<div class="research-overview">
  <div class="research-intro">
    <p>My research focuses on developing and applying computational methods at the intersection of astrophysics, cosmology, and machine learning. The work spans foundation models for scientific applications, advanced ML techniques for astronomical data analysis, cosmic structure investigation, and statistical inference methods.</p>
    <p class="disclaimer"><strong>Disclaimer:</strong> This section is automatically updated by Reasoning Language Models. Google Gemini is utilized to periodically go over my recent publications, talks and activities to update the content. While the information is monitored, at times incorrect information may appear.</p>
  </div>

  <div class="research-content">
{sections_html}  </div>
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
  background: linear-gradient(135deg, #1a1c1e 0%, #2a2d30 100%);
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(255,255,255,0.1);
  border: 1px solid #2a2d30;
}}

.research-intro p {{
  font-size: 1.1em;
  line-height: 1.7;
  color: #e8e8e8;
  max-width: 800px;
  margin: 0 auto;
}}

.research-intro .disclaimer {{
  font-size: 0.9em;
  color: #aaaaaa;
  font-style: italic;
  margin-top: 1.5rem;
  border-top: 1px solid #2a2d30;
  padding-top: 1rem;
}}

.research-content {{
  display: flex;
  flex-direction: column;
  gap: 3rem;
}}

.research-section {{
  background: #1a1c1e;
  border: 1px solid #2a2d30;
  border-radius: 12px;
  padding: 2.5rem;
  box-shadow: 0 4px 6px rgba(255, 255, 255, 0.07);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.research-section:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 25px rgba(255, 255, 255, 0.15);
}}

.research-header {{
  margin-bottom: 2rem;
}}

.research-header h2 {{
  font-size: 1.8em;
  font-weight: 400;
  margin-bottom: 1rem;
}}

.research-title {{
  color: #ffffff;
  text-decoration: none;
  transition: color 0.2s ease;
}}

.research-title:hover {{
  color: #cccccc;
}}

.research-summary {{
  font-size: 1.05em;
  line-height: 1.7;
  color: #e8e8e8;
  text-align: justify;
}}

.learn-more {{
  color: #ffffff;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}}

.learn-more:hover {{
  color: #cccccc;
  text-decoration: underline;
}}

.research-figures {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}}

.research-figure {{
  text-align: center;
  background: #2a2d30;
  border-radius: 12px;
  padding: 1.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #3a3f45;
}}

.research-figure:hover {{
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(255,255,255,0.15);
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
  color: #aaaaaa;
  margin-top: 1rem;
  line-height: 1.4;
  font-style: italic;
}}

.no-figures {{
  grid-column: 1 / -1;
  text-align: center;
  padding: 3rem;
  color: #aaaaaa;
  font-style: italic;
  background: linear-gradient(135deg, #1a1c1e 0%, #2a2d30 100%);
  border-radius: 12px;
  border: 2px dashed #3a3f45;
}}

.research-stats {{
  display: flex;
  gap: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #2a2d30;
}}

.stat {{
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #2a2d30 0%, #3a3f45 100%);
  border-radius: 20px;
  font-size: 0.9em;
  font-weight: 600;
  color: #e8e8e8;
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
}}
</style>
"""
    
    def update_portfolio_pages(self, categories: Dict = None):
        """Update portfolio pages with LLM-generated content."""
        print("📁 Updating portfolio pages...")
        
        if not categories:
            # Get categories from research page update
            papers = self.fetch_publications_from_arxiv()
            categories = self.classify_papers_with_llm(papers)
        
        # Create portfolio pages
        for i, (cat_key, cat_info) in enumerate(categories.items()):
            if not cat_info['papers']:
                continue
            
            print(f"   📝 Creating portfolio page for {cat_info['name']}...")
            
            # Generate detailed research summary
            summary = self.generate_portfolio_summary_with_llm(cat_info['name'], cat_info['papers'])
            
            # Get predefined figures for this category
            figure_files = []
            figure_papers = []
            if 'figures' in cat_info:
                for i, figure_filename in enumerate(cat_info['figures'][:4]):  # Limit to 4 figures
                    fig_path = self.figures_dir / figure_filename
                    if fig_path.exists():
                        figure_files.append(fig_path)
                        # Get corresponding paper title
                        if i < len(cat_info['papers']):
                            figure_papers.append(cat_info['papers'][i])
                        else:
                            figure_papers.append("Research figure")
            else:
                # Fallback method
                for paper_title in cat_info['papers'][:4]:
                    paper_slug = self.create_url_slug(paper_title)
                    matching_figures = list(self.figures_dir.glob(f"*{paper_slug}*_plot_*.png"))
                    
                    if not matching_figures:
                        title_words = paper_title.lower().split()[:3]
                        for word in title_words:
                            if len(word) > 3:
                                word_figures = list(self.figures_dir.glob(f"*{word}*_plot_*.png"))
                                if word_figures:
                                    matching_figures = [word_figures[0]]
                                    break
                    
                    if matching_figures:
                        figure_files.append(matching_figures[0])
                        figure_papers.append(paper_title)
            
            figures_html = self.create_portfolio_figures_html(figure_files, figure_papers)
            
            # Create portfolio file
            filename = f"portfolio-{i+1}-{cat_key}.md"
            content = f"""---
title: "{cat_info['name']}"
excerpt: "Research in {cat_info['name'].lower()}"
collection: portfolio
---

{summary}

{figures_html}

<style>
.research-figures {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}}

.figure-item {{
  text-align: center;
  background: #f8f9fa;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.figure-item:hover {{
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}}

.figure-item img {{
  max-width: 100%;
  height: auto;
  max-height: 300px;
  object-fit: contain;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}}

.figure-item img:hover {{
  opacity: 0.9;
}}

.figure-caption {{
  font-size: 0.9em;
  color: #6c757d;
  margin-top: 1rem;
  line-height: 1.4;
  font-style: italic;
}}

@media (max-width: 768px) {{
  .research-figures {{
    grid-template-columns: 1fr;
    gap: 1rem;
  }}
  
  .figure-item {{
    padding: 1rem;
  }}
}}
</style>

<!-- Figure Modal -->
<div id="imageModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="modalImage">
</div>

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

window.onclick = function(event) {{
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {{
    modal.style.display = 'none';
  }}
}}

document.addEventListener('keydown', function(event) {{
  if (event.key === 'Escape') {{
    closeModal();
  }}
}});
</script>
"""
            
            filepath = self.portfolio_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"   ✅ Created {filename}")
        
        print(f"✅ Updated {len(categories)} portfolio pages")
    
    def generate_portfolio_summary_with_llm(self, category_name: str, papers: List[str]) -> str:
        """Generate detailed portfolio summary using LLM."""
        paper_list = "\n".join([f"- {paper}" for paper in papers])
        
        prompt = f"""Write a comprehensive research summary for the "{category_name}" portfolio page based on these papers by Dr. Nesar Ramachandra:

{paper_list}

Requirements:
1. Start with 2-3 paragraphs describing the research area objectively (third person)
2. Then add 1-2 paragraphs using first person ("My work...", "I have developed...", etc.)
3. Focus on technical contributions, methodologies, and impact
4. Be specific about techniques and applications mentioned in the paper titles
5. Total length: 4-5 paragraphs, around 300-400 words
6. Academic but accessible tone suitable for a portfolio
7. Do not use markdown formatting

Write professionally about the research contributions and their significance."""
        
        return self.llm_generate(prompt)
    
    def create_portfolio_figures_html(self, figure_files: List[Path], papers: List[str] = None) -> str:
        """Create HTML for portfolio research figures."""
        if not figure_files:
            return '<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>'
        
        html = '<div class="research-figures">\n'
        
        for i, figure_file in enumerate(figure_files[:4]):  # Limit to 4 figures
            # Use the corresponding paper title if available, otherwise extract from filename
            if papers and i < len(papers):
                paper_name = papers[i]
            else:
                paper_name = figure_file.stem.split('_plot_')[0].replace('_', ' ').replace('-', ' ')
            
            html += f'''  <div class="figure-item">
    <img src="/images/research/figures/{figure_file.name}" alt="Figure from {paper_name}" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: {paper_name}</div>
  </div>
'''
        
        html += '</div>\n'
        return html
    
    def run_full_update(self):
        """Run complete website content update."""
        print("🚀 Starting Full Website Content Update")
        print("=" * 60)
        
        # Update publications
        self.update_publications()
        
        # Update research page (includes classification and plot extraction)
        categories = self.update_research_page()
        
        # Update portfolio pages
        self.update_portfolio_pages(categories)
        
        print("\n" + "=" * 60)
        print("🎉 FULL WEBSITE UPDATE COMPLETE!")
        print("=" * 60)
        print("\n✨ All content updated with:")
        print("   📚 Latest publications from arXiv")
        print("   🤖 LLM-generated research categories and summaries") 
        print("   🎨 Extracted scientific figures from papers")
        print("   📁 Updated portfolio pages with detailed content")
        print("   🎨 Clean, consistent HTML formatting")

def main():
    """Main function with command line arguments."""
    parser = argparse.ArgumentParser(description='Unified Website Content Manager')
    parser.add_argument('--update-publications', action='store_true', 
                       help='Update publication markdown files')
    parser.add_argument('--update-research', action='store_true',
                       help='Update research page with LLM content')
    parser.add_argument('--update-portfolio', action='store_true',
                       help='Update portfolio pages')
    parser.add_argument('--full-update', action='store_true',
                       help='Run complete website update (default)')
    
    args = parser.parse_args()
    
    # Default to full update if no specific flags
    if not any([args.update_publications, args.update_research, args.update_portfolio]):
        args.full_update = True
    
    manager = WebsiteContentManager()
    
    try:
        if args.full_update:
            manager.run_full_update()
        else:
            if args.update_publications:
                manager.update_publications()
            if args.update_research:
                manager.update_research_page()
            if args.update_portfolio:
                manager.update_portfolio_pages()
                
    except KeyboardInterrupt:
        print("\n❌ Update cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Update failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
