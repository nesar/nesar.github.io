#!/usr/bin/env python3
"""
Complete cleanup and organization script for the research website.
Fixes duplicates, ensures figure diversity, and creates comprehensive publication lists.
"""

import os
import re
import json
from collections import defaultdict
from typing import List, Dict, Set

class ResearchOrganizer:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.pub_dir = os.path.join(self.base_dir, "_publications")
        self.portfolio_dir = os.path.join(self.base_dir, "_portfolio")
        self.figures_dir = os.path.join(self.base_dir, "images", "research", "figures")
        
    def get_all_publications_by_category(self) -> Dict[str, List[Dict]]:
        """Get all publications organized by research category."""
        print("📚 Analyzing all publications...")
        
        categories = {
            'machine-learning': {
                'keywords': ['machine learning', 'deep learning', 'neural network', 'ai ', 'artificial intelligence', 'generative', 'anomaly detection', 'lensing', 'gravitational lens', 'astromlab'],
                'papers': []
            },
            'dark-matter': {
                'keywords': ['dark matter', 'cosmic web', 'cosmology', 'caustic', 'multistream', 'halo', 'structure formation'],
                'papers': []
            },
            'uncertainty-quantification': {
                'keywords': ['uncertainty', 'bayesian', 'probabilistic neural', 'error', 'confidence'],
                'papers': []
            },
            'statistical-emulation': {
                'keywords': ['emulator', 'emulation', 'surrogate', 'reduced order', 'approximation', 'power spectrum', 'synthetic'],
                'papers': []
            },
            'other-research': {
                'keywords': [],
                'papers': []
            }
        }
        
        # Manual classification for accuracy
        manual_classifications = {
            'Multi-stream portrait of the cosmic web': 'dark-matter',
            'Dark matter haloes: a multistream view': 'dark-matter',
            'Topology and geometry of the dark matter web': 'dark-matter',
            'The Caustic Design of the Dark Matter Web': 'dark-matter',
            'Tracing the cosmic web': 'dark-matter',
            'Matter Power Spectrum Emulator': 'statistical-emulation',
            'Matter power spectrum emulator': 'statistical-emulation',
            'Probabilistic neural networks for fluid flow': 'uncertainty-quantification',
            'Probabilistic neural network-based reduced-order': 'statistical-emulation',
            'Application of probabilistic modeling': 'statistical-emulation',
            'Global field reconstruction': 'statistical-emulation',
            'Interpretable Uncertainty Quantification': 'uncertainty-quantification',
            'AstroMLab': 'machine-learning',
            'Anomaly detection': 'machine-learning',
            'Generative networks': 'machine-learning',
            'Machine learning synthetic spectra': 'machine-learning',
            'Neural Network Based Point Spread Function': 'machine-learning',
            'Modular Deep Learning Pipeline': 'machine-learning',
            'Constructing impactful machine learning': 'machine-learning'
        }
        
        # Process all publication files
        for filename in os.listdir(self.pub_dir):
            if not filename.endswith('.md'):
                continue
            
            try:
                with open(os.path.join(self.pub_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract metadata
                title_match = re.search(r'title:\s*["\'](.*?)["\']', content, re.DOTALL)
                date_match = re.search(r'date:\s*([\d-]+)', content)
                venue_match = re.search(r'venue:\s*["\'](.*?)["\']', content)
                
                title = title_match.group(1) if title_match else "Unknown"
                date = date_match.group(1) if date_match else ""
                venue = venue_match.group(1) if venue_match else ""
                
                # Extract year for sorting
                year = date[:4] if date else "Unknown"
                
                paper_info = {
                    'title': title,
                    'date': date,
                    'year': year,
                    'venue': venue,
                    'filename': filename
                }
                
                # Categorize paper
                categorized = False
                title_lower = title.lower()
                
                # Check manual classifications first
                for key_phrase, category in manual_classifications.items():
                    if key_phrase.lower() in title_lower:
                        categories[category]['papers'].append(paper_info)
                        categorized = True
                        break
                
                # Use keyword matching if not manually classified
                if not categorized:
                    for category, category_info in categories.items():
                        if category == 'other-research':
                            continue
                            
                        for keyword in category_info['keywords']:
                            if keyword in title_lower:
                                category_info['papers'].append(paper_info)
                                categorized = True
                                break
                        
                        if categorized:
                            break
                
                if not categorized:
                    categories['other-research']['papers'].append(paper_info)
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        
        # Sort papers by date (newest first)
        for category in categories.values():
            category['papers'].sort(key=lambda x: x['date'], reverse=True)
        
        return categories
    
    def get_figures_by_paper(self) -> Dict[str, List[Dict]]:
        """Get all figures organized by paper."""
        if not os.path.exists(self.figures_dir):
            return {}
        
        figures_by_paper = defaultdict(list)
        
        # Map figure filenames to paper titles
        paper_mappings = {
            'a_modular_deep_learning_pipeline_for_galaxy-scale_': 'A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection and Modeling',
            'anomaly_detection_in_astronomical_images_with_gene': 'Anomaly detection in astronomical images with generative adversarial networks',
            'generative_networks_for_emulating_synthetic_sky_im': 'Generative networks for emulating synthetic sky images',
            'modular_deep_learning_analysis_of_galaxy-scale_str': 'Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images',
            'the_caustic_design_of_the_dark_matter_web': 'The Caustic Design of the Dark Matter Web',
            'probabilistic_neural_networks_for_fluid_flow_model': 'Probabilistic neural networks for fluid flow model-order reduction and data recovery',
            'probabilistic_neural_network-based_reduced-order_s': 'Probabilistic neural network-based reduced-order surrogate for fluid flows',
            'application_of_probabilistic_modeling_and_automate': 'Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field'
        }
        
        for filename in os.listdir(self.figures_dir):
            if not filename.endswith('.png'):
                continue
            
            # Extract paper slug from filename
            parts = filename.split('_')
            paper_parts = []
            for i, part in enumerate(parts):
                if part.startswith('page') and i > 0:
                    break
                paper_parts.append(part)
            
            paper_slug = '_'.join(paper_parts)
            paper_title = paper_mappings.get(paper_slug, paper_slug.replace('_', ' ').title())
            
            figure_info = {
                'filename': filename,
                'relative_path': f"/images/research/figures/{filename}",
                'paper_title': paper_title,
                'paper_slug': paper_slug
            }
            
            figures_by_paper[paper_title].append(figure_info)
        
        return dict(figures_by_paper)
    
    def create_diverse_figure_selection(self, category: str, publications: List[Dict], figures_by_paper: Dict) -> List[Dict]:
        """Select diverse figures from different papers for a category."""
        selected_figures = []
        used_papers = set()
        
        # First pass: one figure from each paper that has figures
        for paper in publications:
            if len(selected_figures) >= 4:
                break
                
            paper_title = paper['title']
            if paper_title in figures_by_paper and paper_title not in used_papers:
                figures = figures_by_paper[paper_title]
                if figures:
                    selected_figures.append(figures[0])  # Take first figure
                    used_papers.add(paper_title)
        
        # Second pass: add more figures from different papers if needed
        if len(selected_figures) < 4:
            for paper in publications:
                if len(selected_figures) >= 4:
                    break
                    
                paper_title = paper['title']
                if paper_title in figures_by_paper:
                    figures = figures_by_paper[paper_title]
                    # Take second figure if we have space
                    if len(figures) > 1 and len(selected_figures) < 4:
                        selected_figures.append(figures[1])
        
        return selected_figures[:4]  # Maximum 4 figures
    
    def create_portfolio_content(self, category: str, title: str, description: str, publications: List[Dict], figures: List[Dict]) -> str:
        """Create clean portfolio content."""
        
        content = f"""---
title: "{title}"
excerpt: "Research in {title.lower()} <br/><img src='/images/research_{category}.png'>"
collection: portfolio
---

{description}

## Research Figures

<div class="research-figures-grid">
"""
        
        for fig in figures:
            content += f"""  <div class="research-figure">
    <img src="{fig['relative_path']}" alt="Figure from {fig['paper_title']}" onclick="openModal(this)">
    <p class="figure-caption">From: {fig['paper_title'][:80]}{'...' if len(fig['paper_title']) > 80 else ''}</p>
  </div>
"""
        
        content += """</div>

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

## Related Publications ({len(publications)} papers):

"""
        
        # Add comprehensive publication list
        for paper in publications:
            year = paper['year'] if paper['year'] != 'Unknown' else ''
            venue_text = f" - {paper['venue']}" if paper['venue'] else ""
            content += f"- **{paper['title']}** ({year}){venue_text}\n"
        
        return content
    
    def create_clean_research_overview(self, categories_with_figures: Dict):
        """Create a clean research overview page without duplicates."""
        
        content = """---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<div class="research-overview">
  <div class="research-intro">
    <p>My research focuses on developing and applying computational methods at the intersection of astrophysics, cosmology, and machine learning. Below are my main research areas with representative figures from recent publications.</p>
  </div>

  <div class="research-gallery">
"""

        research_configs = [
            {
                'category': 'machine-learning',
                'title': 'Machine Learning & AI',
                'description': 'Developing specialized AI models for astronomy, including domain-specific LLMs, neural networks for astronomical data analysis, and generative models for synthetic observations.',
                'icon': '🤖',
                'color': '#3b82f6'
            },
            {
                'category': 'dark-matter',
                'title': 'Dark Matter & Cosmology',
                'description': 'Investigating the cosmic web structure, dark matter halos, and large-scale structure formation using N-body simulations and multi-stream analysis.',
                'icon': '🌌',
                'color': '#8b5cf6'
            },
            {
                'category': 'uncertainty-quantification',
                'title': 'Uncertainty Quantification',
                'description': 'Developing Bayesian and probabilistic methods for robust scientific inference, including uncertainty estimation in machine learning models.',
                'icon': '📊',
                'color': '#ef4444'
            },
            {
                'category': 'statistical-emulation',
                'title': 'Statistical Emulation & Inference',
                'description': 'Developing statistical emulators and surrogate models for cosmological simulations, including power spectrum emulation and reduced-order modeling.',
                'icon': '📈',
                'color': '#f59e0b'
            }
        ]
        
        for config in research_configs:
            category = config['category']
            figures = categories_with_figures.get(category, [])
            
            content += f"""
    <div class="research-area" style="border-left: 4px solid {config['color']};">
      <div class="research-area-header">
        <h2>
          <span class="research-icon">{config['icon']}</span>
          <a href="/portfolio/portfolio-{research_configs.index(config)+1}-{category}/" class="research-title">{config['title']}</a>
        </h2>
        <p class="research-description">{config['description']}</p>
      </div>
      
      <div class="research-preview-figures">
"""
            
            if figures:
                # Show first 2 figures
                for i, fig in enumerate(figures[:2]):
                    content += f"""
        <div class="preview-figure">
          <img src="{fig['relative_path']}" alt="Research preview" onclick="openModal(this)" />
        </div>
"""
                
                if len(figures) > 2:
                    content += f"""
        <div class="more-figures">
          <a href="/portfolio/portfolio-{research_configs.index(config)+1}-{category}/" class="view-more-btn">
            +{len(figures) - 2} more figures →
          </a>
        </div>
"""
            else:
                content += """
        <div class="no-figures">
          <p>Representative figures coming soon...</p>
        </div>
"""
            
            content += """
      </div>
    </div>
"""

        content += """
  </div>
</div>

<!-- Figure Modal -->
<div id="imageModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="modalImage">
</div>

<style>
.research-overview {
  max-width: 1200px;
  margin: 0 auto;
}

.research-intro {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius: 12px;
}

.research-intro p {
  font-size: 1.1em;
  line-height: 1.6;
  color: #4a5568;
  max-width: 800px;
  margin: 0 auto;
}

.research-gallery {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

.research-area {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.research-area:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.research-area-header {
  margin-bottom: 1.5rem;
}

.research-area h2 {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
  font-size: 1.8em;
  font-weight: 700;
}

.research-icon {
  font-size: 1.2em;
}

.research-title {
  color: #2d3748;
  text-decoration: none;
  transition: color 0.2s ease;
}

.research-title:hover {
  color: #3182ce;
}

.research-description {
  font-size: 1.05em;
  line-height: 1.6;
  color: #4a5568;
  margin: 0;
}

.research-preview-figures {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
  align-items: center;
}

.preview-figure {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  background: #f7fafc;
}

.preview-figure img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  cursor: pointer;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.preview-figure img:hover {
  transform: scale(1.05);
  opacity: 0.9;
}

.more-figures {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 200px;
  background: linear-gradient(135deg, #edf2f7 0%, #e2e8f0 100%);
  border-radius: 8px;
  border: 2px dashed #cbd5e0;
}

.view-more-btn {
  display: inline-flex;
  align-items: center;
  padding: 1rem 1.5rem;
  background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.view-more-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(66, 153, 225, 0.4);
  color: white;
}

.no-figures {
  grid-column: 1 / -1;
  text-align: center;
  padding: 2rem;
  color: #718096;
  font-style: italic;
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
  max-width: 900px;
  padding-top: 2%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.3s ease;
}

.close:hover {
  color: #bbb;
}

/* Responsive design */
@media (max-width: 768px) {
  .research-area {
    padding: 1.5rem;
  }
  
  .research-area h2 {
    font-size: 1.5em;
  }
  
  .research-preview-figures {
    grid-template-columns: 1fr;
  }
  
  .preview-figure img {
    height: 150px;
  }
}
</style>

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
"""
        
        return content
    
    def cleanup_and_organize(self):
        """Main cleanup and organization function."""
        print("🧹 Starting complete cleanup and organization...")
        
        # Get all publications by category
        publications_by_category = self.get_all_publications_by_category()
        
        # Get all figures by paper
        figures_by_paper = self.get_figures_by_paper()
        
        # Portfolio configurations
        portfolio_configs = {
            'machine-learning': {
                'title': 'Machine Learning & AI',
                'description': 'Developing specialized AI models for astronomy, including domain-specific LLMs, neural networks for astronomical data analysis, and generative models for synthetic observations.',
                'file': 'portfolio-1-machine-learning.md'
            },
            'dark-matter': {
                'title': 'Dark Matter & Cosmology',
                'description': 'Investigating the cosmic web structure, dark matter halos, and large-scale structure formation using N-body simulations and multi-stream analysis.',
                'file': 'portfolio-2-dark-matter.md'
            },
            'uncertainty-quantification': {
                'title': 'Uncertainty Quantification',
                'description': 'Developing Bayesian and probabilistic methods for robust scientific inference, including uncertainty estimation in machine learning models.',
                'file': 'portfolio-3-uncertainty-quantification.md'
            },
            'statistical-emulation': {
                'title': 'Statistical Emulation & Inference',
                'description': 'Developing statistical emulators and surrogate models for cosmological simulations, including power spectrum emulation and reduced-order modeling techniques.',
                'file': 'portfolio-4-statistical-emulation.md'
            },
            'other-research': {
                'title': 'Other Research',
                'description': 'Additional research projects including computational methods, data analysis techniques, and interdisciplinary applications.',
                'file': 'portfolio-5-other-research.md'
            }
        }
        
        # Track figures used for overview page
        categories_with_figures = {}
        
        # Create clean portfolio files
        for category, config in portfolio_configs.items():
            publications = publications_by_category[category]['papers']
            
            if publications:
                # Get diverse figures for this category
                figures = self.create_diverse_figure_selection(category, publications, figures_by_paper)
                categories_with_figures[category] = figures
                
                # Create portfolio content
                content = self.create_portfolio_content(
                    category, 
                    config['title'], 
                    config['description'], 
                    publications,
                    figures
                )
                
                # Write portfolio file
                filepath = os.path.join(self.portfolio_dir, config['file'])
                
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✅ Created {config['file']} with {len(publications)} papers, {len(figures)} diverse figures")
                    
                except Exception as e:
                    print(f"❌ Error creating {config['file']}: {e}")
            else:
                print(f"⚠️  No publications found for {category}")
        
        # Create clean research overview page
        research_content = self.create_clean_research_overview(categories_with_figures)
        research_file = os.path.join(self.base_dir, "_pages", "research.html")
        
        try:
            with open(research_file, 'w', encoding='utf-8') as f:
                f.write(research_content)
            print("✅ Created clean research overview page (no duplicates)")
        except Exception as e:
            print(f"❌ Error creating research overview: {e}")
        
        print("\n🎉 Cleanup and organization complete!")
        print("\n📊 Summary:")
        for category, config in portfolio_configs.items():
            publications = publications_by_category[category]['papers']
            figures = categories_with_figures.get(category, [])
            if publications:
                print(f"   • {config['title']}: {len(publications)} papers, {len(figures)} diverse figures")

def main():
    organizer = ResearchOrganizer()
    organizer.cleanup_and_organize()

if __name__ == "__main__":
    main()