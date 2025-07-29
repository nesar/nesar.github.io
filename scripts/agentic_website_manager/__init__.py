"""
Agentic Website Manager - A modular AI-powered website content management system.

This package provides a collection of specialized agents that work together to:
- Search and download research papers
- Extract figures and text from PDFs
- Classify papers into research categories
- Generate website content and summaries
- Validate and review generated content

Main Components:
- WebAgent: Handles web searches and paper downloads
- ParseAgent: Extracts figures and text from PDFs
- ContentAgent: Classifies papers and generates content
- CriticAgent: Validates and reviews agent outputs
- Orchestrator: Coordinates all agents in workflows

Usage:
    from agentic_website_manager import WebsiteOrchestrator
    
    orchestrator = WebsiteOrchestrator()
    results = orchestrator.run_full_pipeline()
"""

from .orchestrator import WebsiteOrchestrator
from .web_agent import WebAgent  
from .parse_agent import ParseAgent
from .content_agent import ContentAgent
from .critic_agent import CriticAgent
from .config import config

__version__ = "1.0.0"
__author__ = "Agentic Website Manager"

__all__ = [
    "WebsiteOrchestrator",
    "WebAgent",
    "ParseAgent", 
    "ContentAgent",
    "CriticAgent",
    "config"
]