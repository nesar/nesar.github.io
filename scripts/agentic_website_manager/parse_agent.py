"""
Parse Agent for extracting text and figures from research papers.
Handles PDF processing and figure quality assessment.
"""

import io
import hashlib
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from PIL import Image, ImageStat
import fitz  # PyMuPDF
from langchain.tools import BaseTool, tool
from pydantic import BaseModel, Field

from base_agent import BaseAgent
import config

class FigureExtractionInput(BaseModel):
    pdf_path: str = Field(description="Path to PDF file")
    paper_title: str = Field(description="Title of the paper")

class FigureQualityInput(BaseModel):
    image_bytes: bytes = Field(description="Image data as bytes")
    file_size: int = Field(description="File size in bytes")

@tool
def extract_figures_from_pdf(pdf_path: str, paper_title: str) -> List[Dict]:
    """Extract the best scientific figures from a PDF paper."""
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"   ❌ Could not open PDF: {e}")
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
                
                if _is_good_scientific_figure(image, len(image_bytes)):
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
                        'page': page_num + 1,
                        'image_bytes': image_bytes
                    })
                    
            except Exception:
                continue
    
    doc.close()
    
    # Return only the best figure (limit to 1 per paper)
    all_figures.sort(key=lambda x: x['quality_score'], reverse=True)
    top_figures = all_figures[:1]  # Only take the best figure
    
    extracted_plots = []
    for i, figure in enumerate(top_figures):
        # Since we only extract 1 plot per paper, always use _plot_1
        filename = f"{_create_url_slug(paper_title)}_plot_1_{figure['hash']}.png"
        filepath = config.config.figures_dir / filename
        
        # Skip if this exact file already exists
        if filepath.exists():
            print(f"   ⚠️ Plot already exists: {filename}")
            continue
        
        figure['image'].convert('RGB').save(filepath, "PNG", optimize=True)
        
        plot_info = {
            'filename': filename,
            'paper_title': paper_title,
            'size': figure['size'],
            'page': figure['page'],
            'relative_path': f"/images/research/figures/{filename}",
            'quality_score': figure['quality_score'],
            'local_path': str(filepath)
        }
        
        extracted_plots.append(plot_info)
    
    return extracted_plots

@tool
def assess_figure_quality(image_bytes: bytes, file_size: int) -> Dict:
    """Assess the quality of a scientific figure."""
    try:
        image = Image.open(io.BytesIO(image_bytes))
        
        quality_metrics = {
            'is_good_figure': _is_good_scientific_figure(image, file_size),
            'dimensions': image.size,
            'file_size': file_size,
            'aspect_ratio': image.size[0] / image.size[1],
            'complexity_score': 0
        }
        
        # Calculate complexity score
        try:
            image_rgb = image.convert('RGB') if image.mode != 'RGB' else image
            stat = ImageStat.Stat(image_rgb)
            quality_metrics['complexity_score'] = float(np.mean(stat.var))
        except Exception:
            quality_metrics['complexity_score'] = 0
        
        return quality_metrics
        
    except Exception as e:
        return {
            'is_good_figure': False,
            'error': str(e),
            'dimensions': (0, 0),
            'file_size': file_size,
            'aspect_ratio': 0,
            'complexity_score': 0
        }

@tool
def extract_text_from_pdf(pdf_path: str) -> Dict:
    """Extract text content from PDF for analysis."""
    try:
        doc = fitz.open(pdf_path)
        
        text_content = {
            'full_text': '',
            'abstract': '',
            'conclusions': '',
            'page_count': len(doc)
        }
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            page_text = page.get_text()
            text_content['full_text'] += page_text + '\n'
            
            # Try to extract abstract (usually on first page)
            if page_num == 0 and not text_content['abstract']:
                abstract_match = _extract_section(page_text, 'abstract')
                if abstract_match:
                    text_content['abstract'] = abstract_match
            
            # Try to extract conclusions (usually on last pages)
            if page_num >= len(doc) - 3 and not text_content['conclusions']:
                conclusions_match = _extract_section(page_text, 'conclusion')
                if conclusions_match:
                    text_content['conclusions'] = conclusions_match
        
        doc.close()
        return text_content
        
    except Exception as e:
        return {
            'full_text': '',
            'abstract': '',
            'conclusions': '',
            'page_count': 0,
            'error': str(e)
        }

def _is_good_scientific_figure(image: Image.Image, file_size: int) -> bool:
    """Check if image is a good scientific figure."""
    width, height = image.size
    
    # Size filters
    if width < 250 or height < 150 or file_size < 8000:
        return False
    
    # Aspect ratio filter
    aspect_ratio = width / height
    if aspect_ratio < 0.2 or aspect_ratio > 5.0:
        return False
    
    # Complexity filter (variance in pixel values)
    try:
        image_rgb = image.convert('RGB') if image.mode != 'RGB' else image
        stat = ImageStat.Stat(image_rgb)
        variance = np.mean(stat.var)
        return variance >= 50
    except Exception:
        return False

def _create_url_slug(title: str) -> str:
    """Create URL-friendly slug."""
    import re
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    return re.sub(r'\s+', '-', slug)[:50]

def _extract_section(text: str, section_name: str) -> Optional[str]:
    """Extract a specific section from paper text."""
    import re
    
    # Common patterns for section headers
    patterns = [
        rf"{section_name}\s*:?\s*\n(.+?)(?:\n\s*\n|\n[A-Z]|\Z)",
        rf"{section_name.title()}\s*:?\s*\n(.+?)(?:\n\s*\n|\n[A-Z]|\Z)",
        rf"{section_name.upper()}\s*:?\s*\n(.+?)(?:\n\s*\n|\n[A-Z]|\Z)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()[:500]  # Limit length
    
    return None

class ParseAgent(BaseAgent):
    """
    Agent responsible for parsing PDFs and extracting figures and text content.
    """
    
    def __init__(self):
        tools = [extract_figures_from_pdf, assess_figure_quality, extract_text_from_pdf]
        super().__init__(
            name="ParseAgent",
            description="Extracts figures and text content from research papers",
            tools=tools
        )
        
        # Create agent executor with ReAct prompt
        prompt_template = """You are a document parsing agent responsible for extracting figures and text from research papers.

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
    
    def execute(self, papers: List[Dict], task: str = "extract_figures") -> Dict[str, Any]:
        """
        Execute parsing tasks on papers.
        
        Args:
            papers: List of paper dictionaries with local_path
            task: Task to perform ("extract_figures", "extract_text", or "full_parse")
            
        Returns:
            Dictionary containing parsing results
        """
        
        self.log_start(f"parsing task: {task}")
        
        try:
            results = {
                'success': True,
                'papers_processed': 0,
                'figures_extracted': [],
                'text_extracted': [],
                'errors': []
            }
            
            for paper in papers:
                if not paper.get('local_path') or not Path(paper['local_path']).exists():
                    continue
                
                paper_results = self._process_paper(paper, task)
                results['papers_processed'] += 1
                
                if paper_results.get('figures'):
                    results['figures_extracted'].extend(paper_results['figures'])
                
                if paper_results.get('text'):
                    results['text_extracted'].append(paper_results['text'])
                
                if paper_results.get('error'):
                    results['errors'].append({
                        'paper': paper['title'],
                        'error': paper_results['error']
                    })
            
            self.log_success("parsing", 
                           f"Processed {results['papers_processed']} papers, "
                           f"extracted {len(results['figures_extracted'])} figures")
            
            return results
            
        except Exception as e:
            self.log_error("parsing", e)
            return {
                'success': False,
                'error': str(e),
                'papers_processed': 0,
                'figures_extracted': [],
                'text_extracted': [],
                'errors': []
            }
    
    def _process_paper(self, paper: Dict, task: str) -> Dict[str, Any]:
        """Process a single paper."""
        results = {}
        
        try:
            pdf_path = paper['local_path']
            paper_title = paper['title']
            
            if task in ["extract_figures", "full_parse"]:
                print(f"   🖼️ Extracting figures from: {paper_title[:50]}...")
                figures = self._extract_figures_from_pdf_direct(pdf_path, paper_title)
                results['figures'] = figures
            
            if task in ["extract_text", "full_parse"]:
                print(f"   📄 Extracting text from: {paper_title[:50]}...")
                text = self._extract_text_from_pdf_direct(pdf_path)
                results['text'] = text
            
            return results
            
        except Exception as e:
            return {'error': str(e)}
    
    def _extract_figures_from_pdf_direct(self, pdf_path: str, paper_title: str) -> List[Dict]:
        """Direct implementation of figure extraction without LangChain tool wrapper."""
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"   ❌ Could not open PDF: {e}")
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
                    
                    if _is_good_scientific_figure(image, len(image_bytes)):
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
                            'page': page_num + 1,
                            'image_bytes': image_bytes
                        })
                        
                except Exception:
                    continue
        
        doc.close()
        
        # Return only the best figure (limit to 1 per paper)
        all_figures.sort(key=lambda x: x['quality_score'], reverse=True)
        top_figures = all_figures[:1]  # Only take the best figure
        
        extracted_plots = []
        for i, figure in enumerate(top_figures):
            # Since we only extract 1 plot per paper, always use _plot_1
            filename = f"{_create_url_slug(paper_title)}_plot_1_{figure['hash']}.png"
            filepath = config.config.figures_dir / filename
            
            # Skip if this exact file already exists
            if filepath.exists():
                print(f"   ⚠️ Plot already exists: {filename}")
                continue
            
            figure['image'].convert('RGB').save(filepath, "PNG", optimize=True)
            
            plot_info = {
                'filename': filename,
                'paper_title': paper_title,
                'size': figure['size'],
                'page': figure['page'],
                'relative_path': f"/images/research/figures/{filename}",
                'quality_score': figure['quality_score'],
                'local_path': str(filepath)
            }
            
            extracted_plots.append(plot_info)
        
        return extracted_plots
    
    def _extract_text_from_pdf_direct(self, pdf_path: str) -> Dict:
        """Direct implementation of text extraction without LangChain tool wrapper."""
        try:
            doc = fitz.open(pdf_path)
            
            text_content = {
                'full_text': '',
                'abstract': '',
                'conclusions': '',
                'page_count': len(doc)
            }
            
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                page_text = page.get_text()
                text_content['full_text'] += page_text + '\n'
                
                # Try to extract abstract (usually on first page)
                if page_num == 0 and not text_content['abstract']:
                    abstract_match = _extract_section(page_text, 'abstract')
                    if abstract_match:
                        text_content['abstract'] = abstract_match
                
                # Try to extract conclusions (usually on last pages)
                if page_num >= len(doc) - 3 and not text_content['conclusions']:
                    conclusions_match = _extract_section(page_text, 'conclusion')
                    if conclusions_match:
                        text_content['conclusions'] = conclusions_match
            
            doc.close()
            return text_content
            
        except Exception as e:
            return {
                'full_text': '',
                'abstract': '',
                'conclusions': '',
                'page_count': 0,
                'error': str(e)
            }
    
    def extract_figures_batch(self, papers: List[Dict]) -> List[Dict]:
        """Extract figures from a batch of papers."""
        self.log_start("batch figure extraction")
        
        all_figures = []
        
        for paper in papers:
            if not paper.get('local_path'):
                continue
                
            try:
                figures = extract_figures_from_pdf(paper['local_path'], paper['title'])
                all_figures.extend(figures)
                
            except Exception as e:
                self.log_error(f"figure extraction for {paper['title']}", e)
                continue
        
        self.log_success("batch figure extraction", f"Extracted {len(all_figures)} figures")
        return all_figures