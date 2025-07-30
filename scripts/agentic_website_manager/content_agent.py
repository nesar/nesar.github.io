"""
Content Agent for classifying papers and generating research content.
Handles LLM-based categorization and summary generation.
"""

import json
import re
from typing import Dict, List, Any, Optional
from langchain.tools import BaseTool, tool
from pydantic import BaseModel, Field

from base_agent import BaseAgent
import config

class PaperClassificationInput(BaseModel):
    papers: List[Dict] = Field(description="List of paper dictionaries with titles")

class SummaryGenerationInput(BaseModel):
    category_name: str = Field(description="Name of the research category")
    papers: List[str] = Field(description="List of paper titles in the category")
    summary_type: str = Field(default="brief", description="Type of summary: 'brief' or 'detailed'")

@tool
def classify_papers(papers: List[Dict]) -> Dict:
    """Classify papers into research categories using LLM."""
    paper_titles = [paper['title'] for paper in papers]
    paper_list = "\n".join([f"{i+1}. {title}" for i, title in enumerate(paper_titles)])
    
    prompt = config.config.prompts['paper_classification'].format(paper_list=paper_list)
    
    # This would normally use the LLM through the agent
    # For now, we'll use the fallback classification
    return _create_simple_classification(papers)

@tool
def generate_category_summary(category_name: str, papers: List[str], summary_type: str = "brief") -> str:
    """Generate a summary for a research category."""
    paper_list = "\n".join([f"- {paper}" for paper in papers])
    
    if summary_type == "brief":
        prompt = config.config.prompts['category_summary'].format(
            category_name=category_name,
            paper_list=paper_list
        )
    else:  # detailed
        prompt = config.config.prompts['portfolio_summary'].format(
            category_name=category_name,
            paper_list=paper_list
        )
    
    # This would use the LLM - for now return a placeholder
    return f"Research summary for {category_name} based on {len(papers)} papers."

@tool
def create_research_html(categories: Dict, category_plots: Dict) -> str:
    """Create HTML content for the research page."""
    sections_html = ""
    colors = ['#6366f1', '#3b82f6', '#8b5cf6', '#f59e0b', '#10b981']
    
    for i, (cat_key, cat_info) in enumerate(categories.items()):
        if not cat_info['papers']:
            continue
        
        color = colors[i % len(colors)]
        portfolio_link = f"/portfolio/portfolio-{i+1}-{cat_key}/"
        
        # Get plots for this category
        plots = category_plots.get(cat_key, [])
        
        # Generate plots HTML
        if plots:
            plots_html = ""
            for plot in plots[:3]:  # Max 3 plots
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
        
        # Generate category summary using direct method
        summary = f"Research in {cat_info['name']} encompasses key methodologies and applications in this important field."
        
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
        <span class="stat">{len(plots)} Figures Available</span>
      </div>
    </div>
'''
        sections_html += section_html
    
    return _generate_research_html_template(sections_html)

@tool
def create_portfolio_content(category_key: str, category_info: Dict, figures: List[Dict]) -> str:
    """Create portfolio page content for a research category."""
    # Generate detailed summary using direct method
    summary = f"Research in {category_info['name']} represents a significant area of investigation with {len(category_info['papers'])} publications. This work encompasses important methodologies and applications that advance our understanding in this field. The research contributes to the broader scientific community through innovative approaches and comprehensive analysis of complex problems in {category_info['name'].lower()}."
    
    # Create figures HTML
    figures_html = _create_portfolio_figures_html(figures, category_info['papers'])
    
    content = f"""---
title: "{category_info['name']}"
excerpt: "Research in {category_info['name'].lower()}"
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
    
    return content

def _create_simple_classification(papers: List[Dict]) -> Dict:
    """Simple keyword-based classification as fallback."""
    categories = {
        'foundation-models': {
            'name': 'Foundation Models',
            'description': 'AI foundation models for scientific applications',
            'papers': []
        },
        'machine-learning': {
            'name': 'Machine Learning for Science',
            'description': 'ML techniques for scientific problems',
            'papers': []
        },
        'dark-matter': {
            'name': 'Dark Matter & Cosmology',
            'description': 'Cosmological structure and dark matter research',
            'papers': []
        },
        'emulation-inference': {
            'name': 'Emulation & Inference',
            'description': 'Statistical emulators and inference methods',
            'papers': []
        }
    }
    
    for paper in papers:
        title_lower = paper['title'].lower()
        
        # Check each category's keywords
        assigned = False
        for cat_key, cat_config in config.config.classification_config['categories'].items():
            if any(kw in title_lower for kw in cat_config['keywords']):
                categories[cat_key]['papers'].append(paper['title'])
                assigned = True
                break
        
        # Default to machine learning if no clear match
        if not assigned:
            categories['machine-learning']['papers'].append(paper['title'])
    
    return categories

def _create_portfolio_figures_html(figures: List[Dict], papers: List[str] = None) -> str:
    """Create HTML for portfolio research figures."""
    if not figures:
        return '<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>'
    
    html = '<div class="research-figures">\n'
    
    for i, figure in enumerate(figures[:4]):  # Limit to 4 figures
        # Use the corresponding paper title if available
        if papers and i < len(papers):
            paper_name = papers[i]
        else:
            paper_name = figure.get('paper_title', 'Research Figure')
        
        figure_path = figure.get('relative_path', f"/images/research/figures/{figure.get('filename', '')}")
        
        html += f'''  <div class="figure-item">
    <img src="{figure_path}" alt="Figure from {paper_name}" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: {paper_name}</div>
  </div>
'''
    
    html += '</div>\n'
    return html

def _generate_research_html_template(sections_html: str) -> str:
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

class ContentAgent(BaseAgent):
    """
    Agent responsible for classifying papers and generating research content.
    """
    
    def __init__(self):
        tools = [classify_papers, generate_category_summary, create_research_html, create_portfolio_content]
        super().__init__(
            name="ContentAgent",
            description="Classifies papers and generates research content using LLM",
            tools=tools
        )
        
        # Create agent executor with ReAct prompt
        prompt_template = """You are a content generation agent responsible for classifying research papers and creating summaries.

You have access to the following tools:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Question: {input}
{agent_scratchpad}"""
        
        self.agent_executor = self.create_agent_executor(prompt_template)
    
    def execute(self, papers: List[Dict], figures: List[Dict] = None, task: str = "full_content") -> Dict[str, Any]:
        """
        Execute content generation tasks.
        
        Args:
            papers: List of paper dictionaries
            figures: List of extracted figures
            task: Task to perform ("classify", "generate_html", or "full_content")
            
        Returns:
            Dictionary containing generated content
        """
        
        self.log_start(f"content generation task: {task}")
        
        try:
            results = {
                'success': True,
                'categories': {},
                'research_html': '',
                'portfolio_pages': {},
                'task': task
            }
            
            if task in ["classify", "full_content"]:
                # Classify papers
                categories = self.classify_papers_llm(papers)
                results['categories'] = categories
            
            if task in ["generate_html", "full_content"]:
                # Use existing categories if not classified in this run
                if not results['categories']:
                    results['categories'] = self.classify_papers_llm(papers)
                
                # Organize figures by category
                category_plots = self._organize_figures_by_category(
                    results['categories'], figures or []
                )
                
                # Generate research HTML
                research_html = self._create_research_html_direct(results['categories'], category_plots)
                results['research_html'] = research_html
                
                # Generate portfolio pages
                portfolio_pages = self._generate_portfolio_pages(
                    results['categories'], category_plots
                )
                results['portfolio_pages'] = portfolio_pages
            
            self.log_success("content generation", 
                           f"Generated content for {len(results['categories'])} categories")
            
            return results
            
        except Exception as e:
            self.log_error("content generation", e)
            return {
                'success': False,
                'error': str(e),
                'categories': {},
                'research_html': '',
                'portfolio_pages': {}
            }
    
    def classify_papers_llm(self, papers: List[Dict]) -> Dict:
        """Classify papers using LLM."""
        self.log_start("paper classification")
        
        try:
            # Try LLM classification first
            paper_titles = [paper['title'] for paper in papers]
            paper_list = "\n".join([f"{i+1}. {title}" for i, title in enumerate(paper_titles)])
            
            prompt = config.config.prompts['paper_classification'].format(paper_list=paper_list)
            
            try:
                response = self.llm_generate(prompt)
                # Extract JSON from response
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                if json_start != -1 and json_end != -1:
                    json_str = response[json_start:json_end]
                    categories = json.loads(json_str)
                    self.log_success("LLM classification", f"Classified into {len(categories)} categories")
                    return categories
                else:
                    raise ValueError("Could not parse LLM response")
            except Exception as e:
                self.log_error("LLM classification", e)
                # Fall back to simple classification
                categories = _create_simple_classification(papers)
                self.log_success("fallback classification", f"Used keyword-based classification")
                return categories
            
        except Exception as e:
            self.log_error("paper classification", e)
            return {}
    
    def _generate_category_summary_direct(self, category_name: str, papers: List[str], summary_type: str = "brief") -> str:
        """Direct implementation of summary generation."""
        paper_list = "\n".join([f"- {paper}" for paper in papers])
        
        if summary_type == "brief":
            prompt = config.config.prompts['category_summary'].format(
                category_name=category_name,
                paper_list=paper_list
            )
        else:  # detailed
            prompt = config.config.prompts['portfolio_summary'].format(
                category_name=category_name,
                paper_list=paper_list
            )
        
        try:
            response = self.llm_generate(prompt)
            return response
        except Exception as e:
            # Fallback summary
            return f"Research in {category_name} encompasses {len(papers)} publications covering key methodologies and applications in this important field."
    
    def _organize_figures_by_category(self, categories: Dict, figures: List[Dict]) -> Dict:
        """Organize figures by research category."""
        category_plots = {cat_key: [] for cat_key in categories.keys()}
        
        for figure in figures:
            paper_title = figure.get('paper_title', '')
            
            # Find which category this paper belongs to
            for cat_key, cat_info in categories.items():
                if paper_title in cat_info['papers']:
                    category_plots[cat_key].append(figure)
                    break
        
        return category_plots
    
    def _generate_portfolio_pages(self, categories: Dict, category_plots: Dict) -> Dict:
        """Generate portfolio page content for each category."""
        portfolio_pages = {}
        
        for i, (cat_key, cat_info) in enumerate(categories.items()):
            if not cat_info['papers']:
                continue
            
            figures = category_plots.get(cat_key, [])[:4]  # Max 4 figures per portfolio
            
            content = self._create_portfolio_content_direct(cat_key, cat_info, figures)
            
            filename = f"portfolio-{i+1}-{cat_key}.md"
            portfolio_pages[filename] = content
        
        return portfolio_pages
    
    def _create_portfolio_content_direct(self, category_key: str, category_info: Dict, figures: List[Dict]) -> str:
        """Direct implementation of portfolio content creation."""
        # Generate detailed summary using direct method or LLM
        try:
            summary = self._generate_category_summary_direct(
                category_info['name'], 
                category_info['papers'], 
                summary_type="detailed"
            )
        except Exception:
            summary = f"Research in {category_info['name']} represents a significant area of investigation with {len(category_info['papers'])} publications. This work encompasses important methodologies and applications that advance our understanding in this field. The research contributes to the broader scientific community through innovative approaches and comprehensive analysis of complex problems in {category_info['name'].lower()}."
        
        # Create figures HTML
        figures_html = _create_portfolio_figures_html(figures, category_info['papers'])
        
        content = f"""---
title: "{category_info['name']}"
excerpt: "Research in {category_info['name'].lower()}"
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
        
        return content
    
    def _create_research_html_direct(self, categories: Dict, category_plots: Dict) -> str:
        """Direct implementation of research HTML creation."""
        sections_html = ""
        colors = ['#6366f1', '#3b82f6', '#8b5cf6', '#f59e0b', '#10b981']
        
        for i, (cat_key, cat_info) in enumerate(categories.items()):
            if not cat_info['papers']:
                continue
            
            color = colors[i % len(colors)]
            portfolio_link = f"/portfolio/portfolio-{i+1}-{cat_key}/"
            
            # Get plots for this category
            plots = category_plots.get(cat_key, [])
            
            # Generate plots HTML
            if plots:
                plots_html = ""
                for plot in plots[:3]:  # Max 3 plots
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
            
            # Generate category summary
            try:
                summary = self._generate_category_summary_direct(cat_info['name'], cat_info['papers'])
            except Exception:
                summary = f"Research in {cat_info['name']} encompasses key methodologies and applications in this important field."
            
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
        <span class="stat">{len(plots)} Figures Available</span>
      </div>
    </div>
'''
            sections_html += section_html
        
        return _generate_research_html_template(sections_html)