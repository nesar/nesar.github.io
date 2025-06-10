#!/usr/bin/env python3
"""
Reorganize research portfolios with better figure diversity and new categories.
"""

import os
import re
import json
from collections import defaultdict
from typing import List, Dict

def collect_all_extracted_figures():
    """Collect all figures from the images/research/figures directory."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    figures_dir = os.path.join(base_dir, "images", "research", "figures")
    
    if not os.path.exists(figures_dir):
        return {}
    
    figures_by_paper = defaultdict(list)
    
    for filename in os.listdir(figures_dir):
        if not filename.endswith('.png'):
            continue
        
        # Extract paper slug from filename
        # Format: paper_slug_pageX_figY_hash.png
        parts = filename.split('_')
        
        # Find the paper title part (everything before _pageX)
        paper_parts = []
        for i, part in enumerate(parts):
            if part.startswith('page') and i > 0:
                break
            paper_parts.append(part)
        
        paper_slug = '_'.join(paper_parts)
        
        # Map common paper slugs to readable titles
        paper_titles = {
            'modular_deep_learning_analysis_of_galaxy-scale_str': 'Modular Deep Learning Analysis of Galaxy-Scale Strong Lensing Images',
            'the_caustic_design_of_the_dark_matter_web': 'The Caustic Design of the Dark Matter Web',
            'probabilistic_neural_networks_for_fluid_flow_model': 'Probabilistic neural networks for fluid flow model-order reduction and data recovery',
            'probabilistic_neural_network-based_reduced-order_s': 'Probabilistic neural network-based reduced-order surrogate for fluid flows',
            'application_of_probabilistic_modeling_and_automate': 'Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field',
            'anomaly_detection_in_astronomical_images_with_gene': 'Anomaly detection in astronomical images with generative adversarial networks',
            'generative_networks_for_emulating_synthetic_sky_im': 'Generative networks for emulating synthetic sky images',
            'a_modular_deep_learning_pipeline_for_galaxy-scale_': 'A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection and Modeling'
        }
        
        paper_title = paper_titles.get(paper_slug, paper_slug.replace('_', ' ').title())
        
        figure_info = {
            'filename': filename,
            'filepath': os.path.join(figures_dir, filename),
            'relative_path': f"/images/research/figures/{filename}",
            'paper_title': paper_title,
            'paper_slug': paper_slug
        }
        
        figures_by_paper[paper_title].append(figure_info)
    
    return figures_by_paper

def categorize_papers_and_figures(figures_by_paper: Dict):
    """Categorize papers and their figures into research areas."""
    categories = {
        'statistical-emulation': {
            'keywords': ['emulator', 'emulation', 'surrogate', 'reduced order', 'approximation', 'power spectrum'],
            'papers': []
        },
        'uncertainty-quantification': {
            'keywords': ['probabilistic neural', 'uncertainty', 'bayesian'],
            'papers': []
        },
        'dark-matter': {
            'keywords': ['dark matter', 'cosmic web', 'cosmology', 'caustic', 'multistream'],
            'papers': []
        },
        'machine-learning': {
            'keywords': ['machine learning', 'deep learning', 'neural network', 'ai ', 'artificial intelligence', 'generative', 'anomaly detection', 'lensing', 'gravitational lens'],
            'papers': []
        },
        'other-research': {
            'keywords': [],
            'papers': []
        }
    }
    
    # Manual classification for specific papers
    manual_classifications = {
        'Probabilistic neural networks for fluid flow model-order reduction and data recovery': 'uncertainty-quantification',
        'Probabilistic neural network-based reduced-order surrogate for fluid flows': 'statistical-emulation',
        'Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field': 'statistical-emulation',
        'The Caustic Design of the Dark Matter Web': 'dark-matter'
    }
    
    # Categorize each paper
    for paper_title, figures in figures_by_paper.items():
        title_lower = paper_title.lower()
        categorized = False
        
        # Check manual classifications first
        if paper_title in manual_classifications:
            category = manual_classifications[paper_title]
            categories[category]['papers'].append({
                'title': paper_title,
                'figures': figures
            })
            categorized = True
        else:
            # Use keyword matching
            for category, category_info in categories.items():
                if category == 'other-research':
                    continue
                    
                for keyword in category_info['keywords']:
                    if keyword in title_lower:
                        category_info['papers'].append({
                            'title': paper_title,
                            'figures': figures
                        })
                        categorized = True
                        break
                
                if categorized:
                    break
        
        if not categorized:
            categories['other-research']['papers'].append({
                'title': paper_title,
                'figures': figures
            })
    
    return categories

def curate_diverse_figures(papers: List[Dict], max_figures: int = 4, max_per_paper: int = 2) -> List[Dict]:
    """Select figures from multiple papers to ensure diversity."""
    curated = []
    
    # Round-robin selection from different papers
    for round_num in range(max_per_paper):
        for paper in papers:
            if len(curated) >= max_figures:
                break
                
            if round_num < len(paper['figures']):
                curated.append(paper['figures'][round_num])
        
        if len(curated) >= max_figures:
            break
    
    return curated[:max_figures]

def create_portfolio_content(category_name: str, title: str, description: str, papers: List[Dict]) -> str:
    """Create portfolio content with curated figures."""
    # Select diverse figures
    curated_figures = curate_diverse_figures(papers, max_figures=4, max_per_paper=2)
    
    content = f"""---
title: "{title}"
excerpt: "Research in {title.lower()} <br/><img src='/images/research_{category_name}.png'>"
collection: portfolio
---

{description}

## Research Figures

<div class="research-figures-grid">
"""
    
    for fig in curated_figures:
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

## Related Publications ({sum(len(p['figures']) for p in papers)} figures from {len(papers)} papers):

"""
    
    # Add publication list
    for paper in papers:
        content += f"- **{paper['title']}** ({len(paper['figures'])} figures)\n"
    
    return content

def main():
    """Main function to reorganize research portfolios."""
    print("🔄 Reorganizing research portfolios with diverse figures...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    portfolio_dir = os.path.join(base_dir, "_portfolio")
    
    # Collect all figures
    figures_by_paper = collect_all_extracted_figures()
    print(f"📊 Found {sum(len(figs) for figs in figures_by_paper.values())} figures from {len(figures_by_paper)} papers")
    
    # Categorize papers
    categories = categorize_papers_and_figures(figures_by_paper)
    
    # Create portfolio files
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
    
    for category, config in portfolio_configs.items():
        papers = categories[category]['papers']
        
        if papers:
            content = create_portfolio_content(
                category, 
                config['title'], 
                config['description'], 
                papers
            )
            
            filepath = os.path.join(portfolio_dir, config['file'])
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Created {config['file']} with {len(papers)} papers, {sum(len(p['figures']) for p in papers)} figures")
                
            except Exception as e:
                print(f"❌ Error creating {config['file']}: {e}")
        else:
            print(f"⚠️  No papers found for {category}")
    
    print("\n🎉 Research portfolio reorganization complete!")
    print("\n💡 Summary:")
    for category, config in portfolio_configs.items():
        papers = categories[category]['papers']
        if papers:
            print(f"   • {config['title']}: {len(papers)} papers, {sum(len(p['figures']) for p in papers)} figures")

if __name__ == "__main__":
    main()