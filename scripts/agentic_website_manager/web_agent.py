"""
Web Agent for searching and downloading research papers.
Handles arXiv API interactions and PDF downloads.
"""

import os
import re
import requests
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Any, Optional
from urllib.parse import quote
from langchain.tools import BaseTool, tool
from pydantic import BaseModel, Field

from base_agent import BaseAgent
import config

class ArxivSearchInput(BaseModel):
    search_terms: List[str] = Field(description="List of search terms to query arXiv")
    max_results: int = Field(default=200, description="Maximum number of results to fetch")

class PaperDownloadInput(BaseModel):
    papers: List[Dict] = Field(description="List of paper dictionaries with arxiv_url")

@tool
def search_arxiv_papers(search_terms: List[str], max_results: int = 200) -> List[Dict]:
    """Search for papers on arXiv using provided search terms."""
    all_papers = []
    seen_arxiv_ids = set()
    
    for search_term in search_terms:
        try:
            encoded_search = quote(search_term)
            url = f"{config.config.search_config['arxiv_base_url']}?search_query={encoded_search}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
            
            response = requests.get(url, timeout=config.config.search_config['timeout'])
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
                
                # Check if target author (more flexible matching)
                is_author = any(
                    pattern(author) for pattern in config.config.search_config['author_patterns']
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
                    'title': _clean_text(title.text),
                    'authors': authors,
                    'date': published.text,
                    'abstract': _clean_text(summary.text if summary is not None else ""),
                    'arxiv_url': arxiv_url,
                    'arxiv_id': arxiv_number,
                    'venue': 'arXiv preprint'
                }
                
                all_papers.append(paper)
            
            time.sleep(config.config.search_config['rate_limit_delay'])
            
        except Exception as e:
            print(f"⚠️ Error with search term '{search_term}': {e}")
            continue
    
    return all_papers

@tool
def download_papers(papers: List[Dict]) -> List[Dict]:
    """Download papers that don't exist locally."""
    for paper in papers:
        if not paper.get('arxiv_url'):
            continue
        
        safe_title = re.sub(r'[^\w\s-]', '', paper['title'])
        safe_title = re.sub(r'\s+', '_', safe_title)
        filename = f"{safe_title[:50]}.pdf"
        filepath = config.config.papers_dir / filename
        
        if filepath.exists():
            paper['local_path'] = str(filepath)
            continue
        
        try:
            print(f"   📥 Downloading: {paper['title'][:50]}...")
            headers = {'User-Agent': config.config.search_config['user_agent']}
            
            # Convert arXiv URL to PDF download URL
            pdf_url = paper['arxiv_url']
            if 'arxiv.org/abs/' in pdf_url:
                pdf_url = pdf_url.replace('arxiv.org/abs/', 'arxiv.org/pdf/') + '.pdf'
            elif not pdf_url.endswith('.pdf'):
                pdf_url = pdf_url + '.pdf'
            
            response = requests.get(pdf_url, headers=headers, stream=True, 
                                  timeout=config.config.search_config['timeout'])
            response.raise_for_status()
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            paper['local_path'] = str(filepath)
            print(f"      ✅ Downloaded: {filename}")
            time.sleep(config.config.search_config['rate_limit_delay'])
            
        except Exception as e:
            print(f"      ❌ Failed to download {paper['title'][:30]}: {e}")
            paper['local_path'] = None
    
    return papers

def _clean_text(text: str) -> str:
    """Clean and normalize text."""
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text.strip())
    return text.replace('"', '\\"')

class WebAgent(BaseAgent):
    """
    Agent responsible for web searching and downloading research papers.
    """
    
    def __init__(self):
        tools = [search_arxiv_papers, download_papers]
        super().__init__(
            name="WebAgent",
            description="Searches for and downloads research papers from arXiv",
            tools=tools
        )
        
        # Create agent executor with ReAct prompt
        prompt_template = """You are a web search agent responsible for finding and downloading research papers.

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
    
    def execute(self, task: str = "search_and_download") -> Dict[str, Any]:
        """
        Execute web agent tasks.
        
        Args:
            task: Task to perform ("search", "download", or "search_and_download")
            
        Returns:
            Dictionary containing papers found and downloaded
        """
        
        self.log_start(f"web search and download task: {task}")
        
        try:
            if task == "search" or task == "search_and_download":
                # Search for papers
                papers = self.search_papers()
                
                if task == "search_and_download" and papers:
                    # Download papers
                    papers = self.download_papers(papers)
                
                self.log_success("paper search and download", f"Found {len(papers)} papers")
                return {
                    'success': True,
                    'papers': papers,
                    'count': len(papers)
                }
            
            elif task == "download":
                # This would need papers passed in
                raise ValueError("Download task requires papers to be provided")
            
            else:
                raise ValueError(f"Unknown task: {task}")
                
        except Exception as e:
            self.log_error("web search and download", e)
            return {
                'success': False,
                'error': str(e),
                'papers': []
            }
    
    def search_papers(self) -> List[Dict]:
        """Search for papers using arXiv API."""
        self.log_start("arXiv paper search")
        
        try:
            papers = search_arxiv_papers(config.config.search_config['search_terms'])
            
            self.log_success("arXiv search", f"Found {len(papers)} papers")
            for i, paper in enumerate(papers):
                print(f"   📄 {i+1}. {paper['title'][:60]}...")
                
            return papers
            
        except Exception as e:
            self.log_error("arXiv search", e)
            return []
    
    def download_papers(self, papers: List[Dict]) -> List[Dict]:
        """Download papers to local storage."""
        self.log_start("paper download")
        
        try:
            papers_with_paths = download_papers(papers)
            downloaded_count = sum(1 for p in papers_with_paths if p.get('local_path'))
            
            self.log_success("paper download", f"Downloaded {downloaded_count} papers")
            return papers_with_paths
            
        except Exception as e:
            self.log_error("paper download", e)
            return papers