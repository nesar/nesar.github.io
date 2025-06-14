#!/usr/bin/env python3
"""
Update Portfolio Pages with Research Summaries and Figures
=========================================================
This script updates the individual portfolio pages with:
1. Gemini-generated research summaries (impersonal then first person)
2. Research figures from extracted plots
3. Better formatting and structure
"""

import os
import re
from pathlib import Path
import google.generativeai as genai

class PortfolioUpdater:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.portfolio_dir = self.base_dir / "_portfolio"
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        
        # Initialize Gemini
        api_key = os.getenv('GEMINI_API_KEY')
        if api_key:
            try:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                self.use_gemini = True
                print("✅ Gemini API configured successfully")
            except Exception as e:
                print(f"⚠️  Gemini setup failed: {e}")
                self.use_gemini = False
        else:
            self.use_gemini = False
        
        # Category mappings
        self.categories = {
            'portfolio-1-foundation-models.md': {
                'name': 'Foundation Models',
                'papers': [
                    "AstroMLab 1: Who wins astronomy jeopardy!?",
                    "AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy",
                    "AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A",
                    "EAIRA: Establishing a Methodology for Evaluating AI Models",
                    "Learning Relationships Between Disparate Representations",
                    "The SPTPoL extended cluster survey",
                    "VizieR Online Data Catalog: The SPTpol Extended Cluster Survey"
                ],
                'figures': [
                    'EAIRA_Establishing_a_Methodology_for_Evaluating_AI_plot_1_adce1f78.png',
                    'EAIRA_Establishing_a_Methodology_for_Evaluating_AI_plot_2_205db31f.png',
                    'EAIRA_Establishing_a_Methodology_for_Evaluating_AI_plot_3_1c174bef.png'
                ]
            },
            'portfolio-2-machine-learning.md': {
                'name': 'Machine Learning for Science',
                'papers': [
                    "Anomaly detection in astronomical images with generative adversarial networks",
                    "Neural Network Based Point Spread Function Deconvolution",
                    "A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lensing",
                    "Generative networks for emulating synthetic sky images",
                    "Probabilistic neural networks for fluid flow surrogate modeling",
                    "Global field reconstruction from sparse sensors with Voronoi tessellation",
                    "Efficient mapping between void shapes and stress fields",
                    "Beyond the hubble sequence–exploring galaxy morphology"
                ],
                'figures': [
                    'Neural_Network_Based_Point_Spread_Function_Deconvo_plot_1_96427c88.png',
                    'Neural_Network_Based_Point_Spread_Function_Deconvo_plot_2_ad6f7fae.png',
                    'Neural_Network_Based_Point_Spread_Function_Deconvo_plot_3_4f111230.png'
                ]
            },
            'portfolio-3-dark-matter.md': {
                'name': 'Dark Matter & Cosmology',
                'papers': [
                    "The Caustic Design of the Dark Matter Web",
                    "Topology and geometry of the dark matter web",
                    "MGemu: An emulator for cosmological models beyond general relativity",
                    "Benchmarking AI-evolved cosmological structure formation",
                    "Diffusion model based emulator for synthetic cosmological structures",
                    "Constraining gravity with cosmic shear analysis",
                    "Weak Lensing: Optimal Separation of Scales",
                    "Multi-stream portrait of the cosmic web"
                ],
                'figures': [
                    'The_Caustic_Design_of_the_Dark_Matter_Web_plot_1_1a1bb482.png',
                    'The_Caustic_Design_of_the_Dark_Matter_Web_plot_2_fa373b8f.png',
                    'The_Caustic_Design_of_the_Dark_Matter_Web_plot_3_a3b0a1c0.png'
                ]
            },
            'portfolio-4-emulation-inference.md': {
                'name': 'Emulation & Inference',
                'papers': [
                    "Application of probabilistic modeling and automated machine learning",
                    "Matter Power Spectrum Emulator for f(R) Modified Gravity",
                    "Constraining Early Dark Energy Models with Power Spectra Emulation",
                    "High-dimensional Surrogate Modeling for Image Data",
                    "Interpretable Uncertainty Quantification in AI for HEP",
                    "Scalable Probabilistic Modeling and Machine Learning",
                    "Cosmological analysis pipelines through Neural Networks",
                    "Probabilistic neural network-based reduced-order surrogate"
                ],
                'figures': [
                    'Application_of_probabilistic_modeling_and_automate_plot_1_8f87fb28.png',
                    'Application_of_probabilistic_modeling_and_automate_plot_2_23b6d91f.png',
                    'Application_of_probabilistic_modeling_and_automate_plot_3_f865475d.png',
                    'Probabilistic_neural_network_reduced_order_plot_1_0ea468f8.png',
                    'Probabilistic_neural_network_reduced_order_plot_2_68f5e3f1.png',
                    'Probabilistic_neural_network_reduced_order_plot_3_42cb185f.png'
                ]
            }
        }
    
    def generate_research_summary(self, category_name: str, papers: list) -> str:
        """Generate research summary using Gemini."""
        if not self.use_gemini:
            return self.get_fallback_summary(category_name)
        
        paper_list = "\n".join([f"- {paper}" for paper in papers])
        
        prompt = f"""Write a comprehensive research summary for the "{category_name}" research area based on these papers:

{paper_list}

Requirements:
1. Start with 2-3 paragraphs describing the research area objectively (third person, impersonal)
2. Then add 1-2 paragraphs using first person ("My work...", "I have developed...", etc.)
3. Focus on technical contributions, methodologies, and impact
4. Make it suitable for an academic portfolio page
5. Be specific about techniques and applications mentioned in the paper titles
6. Total length: 4-5 paragraphs, academic but accessible tone

Format as plain text, no markdown headers."""

        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"❌ Failed to generate summary for {category_name}: {e}")
            return self.get_fallback_summary(category_name)
    
    def get_fallback_summary(self, category_name: str) -> str:
        """Fallback summaries if Gemini fails."""
        fallbacks = {
            'Foundation Models': """Foundation models represent a transformative approach to artificial intelligence in scientific applications, particularly in astronomy and astrophysics. This research area focuses on developing specialized large language models (LLMs) that can understand and reason about domain-specific scientific content. The work encompasses comprehensive evaluation methodologies for AI models in scientific contexts, benchmark development for astronomical question-answering, and the creation of robust frameworks for assessing AI performance in research assistance tasks.

The research demonstrates significant advances in model specialization, showing that domain-focused models can achieve performance comparable to much larger general-purpose systems. The evaluation frameworks developed provide crucial infrastructure for responsible AI deployment in scientific workflows, establishing standards for reliability and accuracy assessment.

My work in this area has centered on developing the AstroMLab series of models, which showcase the effectiveness of domain specialization in achieving superior performance on astronomy-related tasks. I have also contributed to establishing rigorous evaluation methodologies through the EAIRA project, providing frameworks that enable systematic assessment of AI capabilities as research assistants. These contributions help bridge the gap between general AI capabilities and the specific needs of scientific research communities.""",

            'Machine Learning for Science': """Machine learning applications in scientific research have revolutionized data analysis across multiple domains, particularly in astronomy, cosmology, and fluid dynamics. This research encompasses diverse methodologies including generative adversarial networks for anomaly detection in astronomical surveys, deep neural networks for point spread function deconvolution, and probabilistic approaches for surrogate modeling in complex physical systems. The work spans from fundamental image processing challenges to sophisticated pattern recognition tasks in large-scale scientific datasets.

Advanced techniques in this area include modular deep learning pipelines for gravitational lensing analysis, neural network-based approaches for synthetic sky image generation, and novel architectures for handling high-dimensional scientific data. The research emphasizes both computational efficiency and scientific accuracy, developing methods that can handle the scale and complexity of modern astronomical surveys while maintaining rigorous uncertainty quantification.

My contributions to this field focus on developing interpretable and efficient machine learning methods for astronomical applications. I have worked extensively on creating modular pipelines that can be adapted across different scientific problems, with particular emphasis on maintaining scientific rigor while leveraging the power of modern deep learning architectures. This work has enabled more accurate and efficient analysis of complex astronomical phenomena, from galaxy morphology classification to cosmological parameter estimation.""",

            'Dark Matter & Cosmology': """Dark matter and cosmological structure formation represent fundamental challenges in understanding the universe's evolution and composition. This research area encompasses computational approaches to modeling large-scale structure, advanced statistical methods for cosmological parameter estimation, and novel techniques for analyzing the cosmic web's topology and geometry. The work integrates theoretical modeling with observational data analysis, employing both traditional statistical methods and cutting-edge machine learning approaches to extract insights from cosmological simulations and survey data.

Key research directions include the development of emulators for cosmological models beyond general relativity, AI-driven approaches for evolving cosmological structures, and sophisticated analyses of weak lensing signals for cluster mass estimation. The research also encompasses detailed studies of cosmic web morphology, multi-stream analysis of dark matter halos, and the application of topological methods to understand large-scale structure formation.

My research in this area has focused on developing innovative computational tools for cosmological analysis, including advanced emulators that enable efficient exploration of parameter spaces in modified gravity models. I have contributed to understanding the complex topology of the cosmic web through novel analytical approaches and have worked on improving weak lensing analysis techniques for more accurate mass estimation. These efforts have advanced our ability to constrain cosmological models and understand the fundamental physics governing structure formation in the universe.""",

            'Emulation & Inference': """Emulation and statistical inference represent critical methodologies for enabling efficient analysis of complex scientific models and extracting reliable information from high-dimensional datasets. This research area focuses on developing surrogate models that can approximate computationally expensive simulations, advanced uncertainty quantification techniques, and probabilistic frameworks for parameter estimation in scientific applications. The work spans multiple domains including cosmology, high-energy physics, and engineering applications, emphasizing the development of robust, scalable methods for scientific inference.

The research encompasses sophisticated approaches including Gaussian process-based emulation, neural network surrogate modeling, and automated machine learning frameworks for handling high-dimensional problems. Key contributions include developing methods for nonlinear dimensionality reduction in scientific datasets, creating efficient emulators for power spectrum analysis in cosmological models, and establishing frameworks for interpretable uncertainty quantification in AI applications for scientific research.

My work in this area has centered on developing probabilistic modeling frameworks that can handle the computational challenges of modern scientific research. I have contributed to creating automated machine learning pipelines that maintain scientific rigor while providing computational efficiency gains. Through this research, I have helped enable more sophisticated analyses of complex models and provided tools that allow researchers to extract reliable inferences from increasingly large and complex scientific datasets."""
        }
        return fallbacks.get(category_name, "Research summary not available.")
    
    def update_portfolio_page(self, filename: str, category_info: dict):
        """Update a single portfolio page."""
        filepath = self.portfolio_dir / filename
        
        if not filepath.exists():
            print(f"❌ Portfolio file not found: {filename}")
            return
        
        print(f"📝 Updating {category_info['name']}...")
        
        # Generate summary
        summary = self.generate_research_summary(category_info['name'], category_info['papers'])
        
        # Create figures HTML
        figures_html = self.create_figures_html(category_info['figures'])
        
        # Create new content
        content = f"""---
title: "{category_info['name']}"
excerpt: "Research in {category_info['name'].lower()}"
collection: portfolio
---

{summary}

## Representative Research Figures

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
        
        # Write updated content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated {category_info['name']}")
    
    def create_figures_html(self, figure_files: list) -> str:
        """Create HTML for research figures."""
        html = '<div class="research-figures">\n'
        
        for i, filename in enumerate(figure_files[:4]):  # Limit to 4 figures
            if (self.figures_dir / filename).exists():
                # Extract paper name from filename
                paper_name = filename.split('_plot_')[0].replace('_', ' ')
                html += f'''  <div class="figure-item">
    <img src="/images/research/figures/{filename}" alt="Figure from {paper_name}" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: {paper_name}</div>
  </div>
'''
        
        html += '</div>\n'
        return html
    
    def run(self):
        """Update all portfolio pages."""
        print("🚀 Updating Portfolio Pages with Research Summaries and Figures\n")
        print("=" * 60)
        
        for filename, category_info in self.categories.items():
            self.update_portfolio_page(filename, category_info)
        
        print("\n" + "=" * 60)
        print("🎉 Portfolio pages updated successfully!")
        print(f"✨ All pages now include:")
        print(f"   📝 Impersonal + first-person research summaries")
        print(f"   🖼️  Research figures with modal viewing")
        print(f"   🎨 Responsive design and styling")

def main():
    updater = PortfolioUpdater()
    updater.run()

if __name__ == "__main__":
    main()