#!/usr/bin/env python3
"""
Create a beautiful research overview page with figure previews.
"""

import os
import re
import random
from typing import List, Dict

def get_figures_from_portfolio(portfolio_file: str) -> List[str]:
    """Extract figure paths from a portfolio file."""
    if not os.path.exists(portfolio_file):
        return []
    
    figures = []
    try:
        with open(portfolio_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract figure paths from img src attributes
        img_pattern = r'<img src="([^"]+)"'
        matches = re.findall(img_pattern, content)
        
        # Take first few figures (limit to 3 per category)
        figures = matches[:3]
        
    except Exception as e:
        print(f"Error reading {portfolio_file}: {e}")
    
    return figures

def get_research_areas() -> List[Dict]:
    """Get all research areas with their details and sample figures."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    portfolio_dir = os.path.join(base_dir, "_portfolio")
    
    research_areas = [
        {
            'id': 'machine-learning',
            'title': 'Machine Learning & AI',
            'description': 'Developing specialized AI models for astronomy, including domain-specific LLMs, neural networks for astronomical data analysis, and generative models for synthetic observations.',
            'icon': '🤖',
            'file': 'portfolio-1-machine-learning.md',
            'color': '#3b82f6'
        },
        {
            'id': 'dark-matter',
            'title': 'Dark Matter & Cosmology', 
            'description': 'Investigating the cosmic web structure, dark matter halos, and large-scale structure formation using N-body simulations and multi-stream analysis.',
            'icon': '🌌',
            'file': 'portfolio-2-dark-matter.md',
            'color': '#8b5cf6'
        },
        {
            'id': 'uncertainty-quantification',
            'title': 'Uncertainty Quantification',
            'description': 'Developing Bayesian and probabilistic methods for robust scientific inference, including uncertainty estimation in machine learning models.',
            'icon': '📊',
            'file': 'portfolio-3-uncertainty-quantification.md',
            'color': '#ef4444'
        },
        {
            'id': 'statistical-emulation',
            'title': 'Statistical Emulation & Inference',
            'description': 'Developing statistical emulators and surrogate models for cosmological simulations, including power spectrum emulation and reduced-order modeling.',
            'icon': '📈',
            'file': 'portfolio-4-statistical-emulation.md',
            'color': '#f59e0b'
        },
        {
            'id': 'other-research',
            'title': 'Other Research',
            'description': 'Additional research projects including computational methods, data analysis techniques, and interdisciplinary applications.',
            'icon': '⚗️',
            'file': 'portfolio-5-other-research.md',
            'color': '#10b981'
        }
    ]
    
    # Add figures to each research area
    for area in research_areas:
        portfolio_path = os.path.join(portfolio_dir, area['file'])
        area['figures'] = get_figures_from_portfolio(portfolio_path)
        area['has_content'] = os.path.exists(portfolio_path)
    
    return research_areas

def create_research_overview_page():
    """Create the main research overview page with figure previews."""
    research_areas = get_research_areas()
    
    # Filter out areas without content or figures for the preview
    preview_areas = [area for area in research_areas if area['has_content']]
    
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

    for area in preview_areas:
        # Create preview section for each research area
        content += f"""
    <div class="research-area" style="border-left: 4px solid {area['color']};">
      <div class="research-area-header">
        <h2>
          <span class="research-icon">{area['icon']}</span>
          <a href="/portfolio/{area['file'].replace('.md', '')}/" class="research-title">{area['title']}</a>
        </h2>
        <p class="research-description">{area['description']}</p>
      </div>
      
      <div class="research-preview-figures">
"""
        
        # Add figure previews if available
        if area['figures']:
            preview_figures = area['figures'][:2]  # Show first 2 figures
            for i, fig_path in enumerate(preview_figures):
                content += f"""
        <div class="preview-figure">
          <img src="{fig_path}" alt="Research preview" onclick="openModal(this)" />
        </div>
"""
            
            if len(area['figures']) > 2:
                content += f"""
        <div class="more-figures">
          <a href="/portfolio/{area['file'].replace('.md', '')}/" class="view-more-btn">
            +{len(area['figures']) - 2} more figures →
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

<!-- Legacy portfolio items for fallback -->
<div class="legacy-portfolio" style="margin-top: 4rem;">
  <h2>Research Areas</h2>
  {% include base_path %}
  {% for post in site.portfolio %}
    {% include archive-single.html %}
  {% endfor %}
</div>
"""

    return content

def main():
    """Main function to create the research overview page."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_file = os.path.join(base_dir, "_pages", "research.html")
    
    print("Creating enhanced research overview page...")
    
    content = create_research_overview_page()
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Enhanced research page created: {output_file}")
        print("\n💡 The page now includes:")
        print("   • Figure previews from each research area")
        print("   • Interactive hover effects and modals")
        print("   • Responsive grid layout")
        print("   • Direct links to detailed research pages")
        
    except Exception as e:
        print(f"❌ Error creating research page: {e}")

if __name__ == "__main__":
    main()