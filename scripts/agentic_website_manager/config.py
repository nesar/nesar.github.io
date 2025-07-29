"""
Configuration file for Agentic Website Manager
Contains all prompts, settings, and configurations in one place for easy editing.
"""

import os
from pathlib import Path
from typing import Dict, List, Any

class AgentConfig:
    """Configuration class containing all agent settings and prompts."""
    
    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or Path(__file__).parent.parent.parent
        self.setup_paths()
        self.setup_llm_config()
        self.setup_prompts()
        self.setup_search_config()
        self.setup_classification_config()
    
    def setup_paths(self):
        """Setup all file paths."""
        self.publications_dir = self.base_dir / "_publications"
        self.portfolio_dir = self.base_dir / "_portfolio"
        self.research_page = self.base_dir / "_pages" / "research.html"
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.papers_dir = self.base_dir / "temp_papers"
        
        # Create directories if they don't exist
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        self.papers_dir.mkdir(parents=True, exist_ok=True)
    
    def setup_llm_config(self):
        """Setup LLM configuration."""
        self.llm_config = {
            'api_key_env': 'GEMINI_API_KEY',
            'model_name': 'gemini-2.5-flash',
            'max_retries': 3,
            'retry_backoff': 2,
            'timeout': 30
        }
    
    def setup_search_config(self):
        """Setup search and web scraping configuration."""
        self.search_config = {
            'arxiv_base_url': 'http://export.arxiv.org/api/query',
            'max_results': 200,
            'timeout': 30,
            'rate_limit_delay': 2,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'search_terms': [
                'au:"Nesar S Ramachandra"',
                'au:"Ramachandra, Nesar"', 
                'au:"N S Ramachandra"',
                'au:Ramachandra AND au:Nesar',
                'au:"Ramachandra, N S"',
                'au:"Ramachandra, N.S."',
                'au:"N.S. Ramachandra"',
                'au:"Nesar Ramachandra"'
            ],
            'author_patterns': [
                lambda author: "Ramachandra" in author and "Nesar" in author,
                lambda author: "Ramachandra" in author and "N" in author,
                lambda author: "Ramachandra" in author and author.count("N.") > 0,
                lambda author: "N. S. Ramachandra" in author,
                lambda author: "N.S. Ramachandra" in author
            ]
        }
    
    def setup_classification_config(self):
        """Setup paper classification configuration."""
        self.classification_config = {
            'categories': {
                'foundation-models': {
                    'name': 'Foundation Models',
                    'description': 'AI foundation models for scientific applications',
                    'keywords': ['eaira', 'astromllab', 'gpt', 'llm', 'foundation', 'evaluation', 'ai']
                },
                'machine-learning': {
                    'name': 'Machine Learning for Science',
                    'description': 'ML techniques for scientific problems',
                    'keywords': ['neural', 'machine learning', 'deep learning', 'network', 'probabilistic']
                },
                'dark-matter': {
                    'name': 'Dark Matter & Cosmology',
                    'description': 'Cosmological structure and dark matter research',
                    'keywords': ['cosmic', 'cosmology', 'dark matter', 'caustic', 'universe', 'multi-stream']
                },
                'emulation-inference': {
                    'name': 'Emulation & Inference',
                    'description': 'Statistical emulators and inference methods',
                    'keywords': ['emulator', 'inference', 'modeling', 'surrogate', 'reduced']
                }
            }
        }
    
    def setup_prompts(self):
        """Setup all LLM prompts."""
        self.prompts = {
            'paper_classification': """Analyze these research papers and classify them into 4 research categories. Provide a JSON response with category keys, names, descriptions, and paper assignments:

{paper_list}

Return JSON in this exact format:
{{
  "foundation-models": {{
    "name": "Foundation Models",
    "description": "Brief description",
    "papers": ["paper title 1", "paper title 2"]
  }},
  "machine-learning": {{
    "name": "Machine Learning for Science", 
    "description": "Brief description",
    "papers": ["paper title 3"]
  }},
  "dark-matter": {{
    "name": "Dark Matter & Cosmology",
    "description": "Brief description", 
    "papers": ["paper title 4"]
  }},
  "emulation-inference": {{
    "name": "Emulation & Inference",
    "description": "Brief description",
    "papers": ["paper title 5"]
  }}
}}

Assign each paper to the most appropriate category. Each paper should appear exactly once.""",

            'category_summary': """Write a 100-word summary for {category_name} research based on these papers:

{paper_list}

Focus on key methods and impact. Academic tone, no markdown.""",

            'portfolio_summary': """Write a comprehensive research summary for the "{category_name}" portfolio page based on these papers by Dr. Nesar Ramachandra:

{paper_list}

Requirements:
1. Start with 2-3 paragraphs describing the research area objectively (third person)
2. Then add 1-2 paragraphs using first person ("My work...", "I have developed...", etc.)
3. Focus on technical contributions, methodologies, and impact
4. Be specific about techniques and applications mentioned in the paper titles
5. Total length: 4-5 paragraphs, around 300-400 words
6. Academic but accessible tone suitable for a portfolio
7. Do not use markdown formatting

Write professionally about the research contributions and their significance.""",

            'validation_check': """Review this research classification and content generation for accuracy and completeness:

Classification Results:
{classification_results}

Generated Content:
{generated_content}

Check for:
1. Accurate paper categorization
2. Appropriate technical descriptions
3. Consistent formatting
4. Missing or duplicate content
5. Factual accuracy based on paper titles

Provide a brief assessment and any recommended corrections."""
        }

# Global configuration instance
config = AgentConfig()