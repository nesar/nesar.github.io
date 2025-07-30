"""
Critic Agent for validating and reviewing the work of other agents.
Ensures quality, accuracy, and completeness of generated content.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from langchain.tools import BaseTool, tool
from pydantic import BaseModel, Field

from base_agent import BaseAgent
import config

class ValidationInput(BaseModel):
    classification_results: Dict = Field(description="Paper classification results to validate")
    generated_content: Dict = Field(description="Generated content to validate")

class QualityCheckInput(BaseModel):
    content_type: str = Field(description="Type of content to check: 'html', 'markdown', 'json'")
    content: str = Field(description="Content to check for quality")

class ConsistencyCheckInput(BaseModel):
    papers: List[Dict] = Field(description="List of papers")
    categories: Dict = Field(description="Classification categories")
    figures: List[Dict] = Field(description="Extracted figures")

@tool
def validate_classification(classification_results: Dict, papers: List[Dict]) -> Dict:
    """Validate paper classification results for accuracy and completeness."""
    validation_report = {
        'is_valid': True,
        'issues': [],
        'warnings': [],
        'statistics': {},
        'recommendations': []
    }
    
    try:
        # Check if all papers are classified
        all_paper_titles = {paper['title'] for paper in papers}
        classified_papers = set()
        
        for cat_key, cat_info in classification_results.items():
            if 'papers' in cat_info:
                classified_papers.update(cat_info['papers'])
        
        # Find missing papers
        missing_papers = all_paper_titles - classified_papers
        if missing_papers:
            validation_report['issues'].append({
                'type': 'missing_papers',
                'message': f"Papers not classified: {list(missing_papers)[:5]}...",
                'count': len(missing_papers)
            })
            validation_report['is_valid'] = False
        
        # Find duplicate classifications
        paper_counts = {}
        for cat_key, cat_info in classification_results.items():
            for paper in cat_info.get('papers', []):
                paper_counts[paper] = paper_counts.get(paper, 0) + 1
        
        duplicates = {paper: count for paper, count in paper_counts.items() if count > 1}
        if duplicates:
            validation_report['issues'].append({
                'type': 'duplicate_classifications',
                'message': f"Papers classified multiple times: {list(duplicates.keys())[:3]}...",
                'duplicates': duplicates
            })
            validation_report['is_valid'] = False
        
        # Check category balance
        category_sizes = {cat_key: len(cat_info.get('papers', [])) 
                         for cat_key, cat_info in classification_results.items()}
        
        if category_sizes:
            max_size = max(category_sizes.values())
            min_size = min(category_sizes.values())
            
            if max_size > min_size * 3:  # Warn if categories are very imbalanced
                validation_report['warnings'].append({
                    'type': 'imbalanced_categories',
                    'message': f"Categories are imbalanced: {category_sizes}",
                    'details': category_sizes
                })
        
        # Statistics
        validation_report['statistics'] = {
            'total_papers': len(all_paper_titles),
            'classified_papers': len(classified_papers),
            'categories': len(classification_results),
            'category_sizes': category_sizes,
            'coverage': len(classified_papers) / len(all_paper_titles) if all_paper_titles else 0
        }
        
        # Recommendations
        if validation_report['issues']:
            validation_report['recommendations'].append(
                "Re-run classification with improved prompts or manual review"
            )
        
        if validation_report['warnings']:
            validation_report['recommendations'].append(
                "Consider manual rebalancing of categories if appropriate"
            )
        
        return validation_report
        
    except Exception as e:
        validation_report['is_valid'] = False
        validation_report['issues'].append({
            'type': 'validation_error',
            'message': f"Error during validation: {str(e)}"
        })
        return validation_report

@tool
def check_content_quality(content_type: str, content: str) -> Dict:
    """Check the quality of generated content."""
    quality_report = {
        'is_valid': True,
        'issues': [],
        'warnings': [],
        'metrics': {},
        'suggestions': []
    }
    
    try:
        if content_type == 'html':
            quality_report.update(_check_html_quality(content))
        elif content_type == 'markdown':
            quality_report.update(_check_markdown_quality(content))
        elif content_type == 'json':
            quality_report.update(_check_json_quality(content))
        else:
            quality_report.update(_check_text_quality(content))
        
        return quality_report
        
    except Exception as e:
        quality_report['is_valid'] = False
        quality_report['issues'].append({
            'type': 'quality_check_error',
            'message': f"Error during quality check: {str(e)}"
        })
        return quality_report

@tool
def check_data_consistency(papers: List[Dict], categories: Dict, figures: List[Dict]) -> Dict:
    """Check consistency across all data and generated content."""
    consistency_report = {
        'is_consistent': True,
        'issues': [],
        'warnings': [],
        'cross_references': {},
        'suggestions': []
    }
    
    try:
        # Check paper-category consistency
        paper_titles = {paper['title'] for paper in papers}
        categorized_titles = set()
        
        for cat_info in categories.values():
            categorized_titles.update(cat_info.get('papers', []))
        
        # Check for papers in categories but not in original list
        extra_in_categories = categorized_titles - paper_titles
        if extra_in_categories:
            consistency_report['issues'].append({
                'type': 'extra_papers_in_categories',
                'message': f"Papers in categories but not in original list: {list(extra_in_categories)[:3]}...",
                'count': len(extra_in_categories)
            })
            consistency_report['is_consistent'] = False
        
        # Check figure-paper consistency
        figure_papers = {fig.get('paper_title') for fig in figures if fig.get('paper_title')}
        missing_paper_figures = figure_papers - paper_titles
        
        if missing_paper_figures:
            consistency_report['warnings'].append({
                'type': 'figures_for_unknown_papers',
                'message': f"Figures for papers not in list: {list(missing_paper_figures)[:3]}...",
                'count': len(missing_paper_figures)
            })
        
        # Check for papers without figures
        papers_without_figures = paper_titles - figure_papers
        if papers_without_figures:
            consistency_report['warnings'].append({
                'type': 'papers_without_figures',
                'message': f"Papers without extracted figures: {len(papers_without_figures)} papers",
                'count': len(papers_without_figures)
            })
        
        # Cross-reference statistics
        consistency_report['cross_references'] = {
            'papers_total': len(paper_titles),
            'papers_categorized': len(categorized_titles),
            'papers_with_figures': len(figure_papers),
            'figures_total': len(figures),
            'categories_total': len(categories)
        }
        
        return consistency_report
        
    except Exception as e:
        consistency_report['is_consistent'] = False
        consistency_report['issues'].append({
            'type': 'consistency_check_error',
            'message': f"Error during consistency check: {str(e)}"
        })
        return consistency_report

@tool
def generate_validation_report(validation_results: Dict) -> str:
    """Generate a comprehensive validation report."""
    report_lines = []
    report_lines.append("=" * 60)
    report_lines.append("AGENTIC WEBSITE MANAGER - VALIDATION REPORT")
    report_lines.append("=" * 60)
    
    # Overall status
    overall_valid = all([
        validation_results.get('classification_valid', True),
        validation_results.get('content_quality_valid', True),
        validation_results.get('consistency_valid', True)
    ])
    
    status_emoji = "✅" if overall_valid else "❌"
    report_lines.append(f"\n{status_emoji} OVERALL STATUS: {'VALID' if overall_valid else 'ISSUES FOUND'}")
    
    # Classification validation
    if 'classification_validation' in validation_results:
        cv = validation_results['classification_validation']
        report_lines.append(f"\n📊 CLASSIFICATION VALIDATION")
        report_lines.append(f"   Status: {'✅ Valid' if cv['is_valid'] else '❌ Issues found'}")
        
        if cv.get('statistics'):
            stats = cv['statistics']
            report_lines.append(f"   Coverage: {stats['coverage']:.1%} ({stats['classified_papers']}/{stats['total_papers']} papers)")
            report_lines.append(f"   Categories: {stats['categories']}")
        
        if cv.get('issues'):
            report_lines.append("   Issues:")
            for issue in cv['issues'][:3]:  # Show top 3 issues
                report_lines.append(f"     • {issue['message']}")
        
        if cv.get('warnings'):
            report_lines.append("   Warnings:")
            for warning in cv['warnings'][:2]:  # Show top 2 warnings
                report_lines.append(f"     • {warning['message']}")
    
    # Content quality
    if 'content_quality' in validation_results:
        cq = validation_results['content_quality']
        report_lines.append(f"\n📝 CONTENT QUALITY")
        report_lines.append(f"   Status: {'✅ Valid' if cq['is_valid'] else '❌ Issues found'}")
        
        if cq.get('metrics'):
            for metric, value in cq['metrics'].items():
                report_lines.append(f"   {metric}: {value}")
        
        if cq.get('issues'):
            report_lines.append("   Issues:")
            for issue in cq['issues'][:3]:
                report_lines.append(f"     • {issue.get('message', str(issue))}")
    
    # Consistency check
    if 'consistency_check' in validation_results:
        cc = validation_results['consistency_check']
        report_lines.append(f"\n🔗 DATA CONSISTENCY")
        report_lines.append(f"   Status: {'✅ Consistent' if cc['is_consistent'] else '❌ Issues found'}")
        
        if cc.get('cross_references'):
            refs = cc['cross_references']
            report_lines.append(f"   Papers: {refs['papers_total']} total, {refs['papers_categorized']} categorized, {refs['papers_with_figures']} with figures")
            report_lines.append(f"   Figures: {refs['figures_total']} total")
            report_lines.append(f"   Categories: {refs['categories_total']} total")
        
        if cc.get('issues'):
            report_lines.append("   Issues:")
            for issue in cc['issues'][:3]:
                report_lines.append(f"     • {issue['message']}")
    
    # Recommendations
    all_recommendations = []
    for key in ['classification_validation', 'content_quality', 'consistency_check']:
        if key in validation_results and validation_results[key].get('recommendations'):
            all_recommendations.extend(validation_results[key]['recommendations'])
        if key in validation_results and validation_results[key].get('suggestions'):
            all_recommendations.extend(validation_results[key]['suggestions'])
    
    if all_recommendations:
        report_lines.append(f"\n💡 RECOMMENDATIONS")
        for i, rec in enumerate(set(all_recommendations)[:5], 1):  # Top 5 unique recommendations
            report_lines.append(f"   {i}. {rec}")
    
    report_lines.append("\n" + "=" * 60)
    
    return "\n".join(report_lines)

def _check_html_quality(content: str) -> Dict:
    """Check HTML content quality."""
    issues = []
    warnings = []
    metrics = {'length': len(content)}
    
    # Check for basic HTML structure
    if not re.search(r'<div|<section|<article', content, re.IGNORECASE):
        warnings.append({'type': 'no_structure', 'message': 'No structural HTML elements found'})
    
    # Check for missing alt text
    img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
    imgs_without_alt = [img for img in img_tags if 'alt=' not in img]
    if imgs_without_alt:
        issues.append({'type': 'missing_alt', 'message': f'{len(imgs_without_alt)} images missing alt text'})
    
    # Check for broken internal links
    internal_links = re.findall(r'href=["\']([^"\']*)["\']', content)
    broken_links = [link for link in internal_links if link.startswith('/') and not link.startswith('//')]
    if broken_links:
        warnings.append({'type': 'internal_links', 'message': f'{len(broken_links)} internal links found'})
    
    metrics['images'] = len(img_tags)
    metrics['links'] = len(internal_links)
    
    return {
        'is_valid': len(issues) == 0,
        'issues': issues,
        'warnings': warnings,
        'metrics': metrics
    }

def _check_markdown_quality(content: str) -> Dict:
    """Check Markdown content quality."""
    issues = []
    warnings = []
    metrics = {'length': len(content), 'lines': len(content.split('\n'))}
    
    # Check for front matter
    if not content.startswith('---'):
        warnings.append({'type': 'no_frontmatter', 'message': 'No Jekyll front matter found'})
    
    # Check for headings
    headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
    metrics['headings'] = len(headings)
    
    if not headings:
        warnings.append({'type': 'no_headings', 'message': 'No headings found'})
    
    # Check for images
    images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
    metrics['images'] = len(images)
    
    return {
        'is_valid': len(issues) == 0,
        'issues': issues,
        'warnings': warnings,
        'metrics': metrics
    }

def _check_json_quality(content: str) -> Dict:
    """Check JSON content quality."""
    issues = []
    warnings = []
    metrics = {}
    
    try:
        data = json.loads(content)
        metrics['keys'] = len(data) if isinstance(data, dict) else 0
        metrics['valid_json'] = True
    except json.JSONDecodeError as e:
        issues.append({'type': 'invalid_json', 'message': f'Invalid JSON: {str(e)}'})
        metrics['valid_json'] = False
    
    return {
        'is_valid': len(issues) == 0,
        'issues': issues,
        'warnings': warnings,
        'metrics': metrics
    }

def _check_text_quality(content: str) -> Dict:
    """Check general text content quality."""
    issues = []
    warnings = []
    metrics = {
        'length': len(content),
        'words': len(content.split()),
        'sentences': len(re.findall(r'[.!?]+', content))
    }
    
    # Check for reasonable length
    if len(content) < 100:
        warnings.append({'type': 'short_content', 'message': 'Content is very short'})
    
    # Check for repeated content
    sentences = re.findall(r'[^.!?]*[.!?]', content)
    if len(sentences) != len(set(sentences)):
        warnings.append({'type': 'repeated_sentences', 'message': 'Some sentences are repeated'})
    
    return {
        'is_valid': len(issues) == 0,
        'issues': issues,
        'warnings': warnings,
        'metrics': metrics
    }

class CriticAgent(BaseAgent):
    """
    Agent responsible for validating and critiquing the work of other agents.
    """
    
    def __init__(self):
        tools = [validate_classification, check_content_quality, check_data_consistency, generate_validation_report]
        super().__init__(
            name="CriticAgent",
            description="Validates and reviews the work of other agents for quality and accuracy",
            tools=tools
        )
        
        # Create agent executor with ReAct prompt
        prompt_template = """You are a critic agent responsible for validating and reviewing the work of other agents.

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
    
    def execute(self, validation_data: Dict, task: str = "full_validation") -> Dict[str, Any]:
        """
        Execute validation tasks on generated content.
        
        Args:
            validation_data: Dictionary containing data to validate
            task: Task to perform ("validate_classification", "check_quality", "check_consistency", or "full_validation")
            
        Returns:
            Dictionary containing validation results
        """
        
        self.log_start(f"validation task: {task}")
        
        try:
            results = {
                'success': True,
                'task': task,
                'overall_valid': True,
                'validation_report': ''
            }
            
            validation_results = {}
            
            if task in ["validate_classification", "full_validation"]:
                if 'papers' in validation_data and 'categories' in validation_data:
                    classification_result = validate_classification(
                        validation_data['categories'], 
                        validation_data['papers']
                    )
                    validation_results['classification_validation'] = classification_result
                    results['classification_valid'] = classification_result['is_valid']
            
            if task in ["check_quality", "full_validation"]:
                if 'content' in validation_data:
                    for content_type, content in validation_data['content'].items():
                        quality_result = check_content_quality(content_type, content)
                        validation_results[f'{content_type}_quality'] = quality_result
                        if not quality_result['is_valid']:
                            results['overall_valid'] = False
            
            if task in ["check_consistency", "full_validation"]:
                if all(key in validation_data for key in ['papers', 'categories', 'figures']):
                    consistency_result = check_data_consistency(
                        validation_data['papers'],
                        validation_data['categories'],
                        validation_data['figures']
                    )
                    validation_results['consistency_check'] = consistency_result
                    results['consistency_valid'] = consistency_result['is_consistent']
            
            # Generate comprehensive report
            validation_report = generate_validation_report(validation_results)
            results['validation_report'] = validation_report
            results['detailed_results'] = validation_results
            
            # Determine overall validity
            results['overall_valid'] = all([
                results.get('classification_valid', True),
                results.get('consistency_valid', True),
                all(v.get('is_valid', True) for k, v in validation_results.items() if k.endswith('_quality'))
            ])
            
            status = "VALID" if results['overall_valid'] else "ISSUES FOUND"
            self.log_success("validation", f"Validation complete - {status}")
            
            return results
            
        except Exception as e:
            self.log_error("validation", e)
            return {
                'success': False,
                'error': str(e),
                'overall_valid': False,
                'validation_report': f"Validation failed: {str(e)}"
            }
    
    def quick_validation(self, papers: List[Dict], categories: Dict) -> bool:
        """Perform a quick validation check."""
        try:
            result = validate_classification(categories, papers)
            return result['is_valid']
        except Exception:
            return False
    
    def print_validation_report(self, validation_results: Dict):
        """Print validation report to console."""
        if 'validation_report' in validation_results:
            print(validation_results['validation_report'])
        else:
            print("No validation report available")