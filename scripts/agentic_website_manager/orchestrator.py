"""
Orchestrator for coordinating all agents in the website content management system.
Uses LangGraph for complex multi-agent workflows.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import argparse

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent))

import config
from web_agent import WebAgent
from parse_agent import ParseAgent
from content_agent import ContentAgent
from critic_agent import CriticAgent

class WebsiteOrchestrator:
    """
    Main orchestrator class that coordinates all agents to manage website content.
    """
    
    def __init__(self):
        self.setup_agents()
        self.results = {}
        
    def setup_agents(self):
        """Initialize all agents."""
        print("🚀 Initializing Agentic Website Manager...")
        print("=" * 60)
        
        try:
            self.web_agent = WebAgent()
            print("✅ WebAgent initialized")
            
            self.parse_agent = ParseAgent()
            print("✅ ParseAgent initialized")
            
            self.content_agent = ContentAgent()
            print("✅ ContentAgent initialized")
            
            self.critic_agent = CriticAgent()
            print("✅ CriticAgent initialized")
            
            print("=" * 60)
            print("🎯 All agents ready for operation")
            
        except Exception as e:
            print(f"❌ Failed to initialize agents: {e}")
            raise
    
    def run_full_pipeline(self, validate: bool = True) -> Dict[str, Any]:
        """
        Run the complete website content generation pipeline.
        
        Args:
            validate: Whether to run validation checks
            
        Returns:
            Dictionary containing all results
        """
        
        print("\n🚀 Starting Full Website Content Pipeline")
        print("=" * 60)
        
        pipeline_results = {
            'start_time': datetime.now(),
            'success': True,
            'stages': {},
            'final_results': {}
        }
        
        try:
            # Stage 1: Web Search and Download
            print("\n📡 STAGE 1: Web Search and Paper Download")
            print("-" * 40)
            
            web_results = self.web_agent.execute("search_and_download")
            pipeline_results['stages']['web_search'] = web_results
            
            if not web_results['success'] or not web_results['papers']:
                raise Exception("Failed to find or download papers")
            
            papers = web_results['papers']
            print(f"✅ Found and processed {len(papers)} papers")
            
            # Stage 2: Parse and Extract Figures
            print("\n🖼️ STAGE 2: Parse PDFs and Extract Figures")
            print("-" * 40)
            
            parse_results = self.parse_agent.execute(papers, "extract_figures")
            pipeline_results['stages']['parsing'] = parse_results
            
            if not parse_results['success']:
                print("⚠️ Parsing had issues, continuing with available data")
            
            figures = parse_results['figures_extracted']
            print(f"✅ Extracted {len(figures)} figures from papers")
            
            # Stage 3: Classify Papers and Generate Content
            print("\n📝 STAGE 3: Classify Papers and Generate Content")
            print("-" * 40)
            
            content_results = self.content_agent.execute(papers, figures, "full_content")
            pipeline_results['stages']['content_generation'] = content_results
            
            if not content_results['success']:
                raise Exception("Failed to generate content")
            
            categories = content_results['categories']
            print(f"✅ Classified papers into {len(categories)} categories")
            
            # Stage 4: Validation (if requested)
            if validate:
                print("\n🔍 STAGE 4: Validation and Quality Check")
                print("-" * 40)
                
                validation_data = {
                    'papers': papers,
                    'categories': categories,
                    'figures': figures,
                    'content': {
                        'html': content_results.get('research_html', ''),
                        'json': str(categories)
                    }
                }
                
                validation_results = self.critic_agent.execute(validation_data, "full_validation")
                pipeline_results['stages']['validation'] = validation_results
                
                if validation_results['success']:
                    print("✅ Validation completed")
                    self.critic_agent.print_validation_report(validation_results)
                else:
                    print("⚠️ Validation had issues")
            
            # Stage 5: Write Files
            print("\n💾 STAGE 5: Writing Generated Content to Files")
            print("-" * 40)
            
            file_results = self._write_generated_files(content_results, papers)
            pipeline_results['stages']['file_writing'] = file_results
            
            if file_results['success']:
                print(f"✅ Successfully wrote {file_results['files_written']} files")
            else:
                print("⚠️ Some files could not be written")
            
            # Final results
            pipeline_results['final_results'] = {
                'papers_processed': len(papers),
                'figures_extracted': len(figures),
                'categories_created': len(categories),
                'files_written': file_results.get('files_written', 0),
                'validation_passed': validation_results.get('overall_valid', True) if validate else True
            }
            
            pipeline_results['end_time'] = datetime.now()
            pipeline_results['duration'] = pipeline_results['end_time'] - pipeline_results['start_time']
            
            print("\n" + "=" * 60)
            print("🎉 PIPELINE COMPLETED SUCCESSFULLY!")
            print("=" * 60)
            self._print_final_summary(pipeline_results)
            
            return pipeline_results
            
        except Exception as e:
            pipeline_results['success'] = False
            pipeline_results['error'] = str(e)
            pipeline_results['end_time'] = datetime.now()
            
            print(f"\n❌ PIPELINE FAILED: {e}")
            print("=" * 60)
            
            return pipeline_results
    
    def run_research_only_update(self, validate: bool = True) -> Dict[str, Any]:
        """
        Run research and portfolio update only (preserve publications).
        
        Args:
            validate: Whether to run validation checks
            
        Returns:
            Dictionary containing results
        """
        
        print("\n🔬 Starting Research-Only Update Pipeline")
        print("=" * 60)
        
        pipeline_results = {
            'start_time': datetime.now(),
            'success': True,
            'stages': {},
            'final_results': {}
        }
        
        try:
            # Get papers (without downloading)
            web_results = self.web_agent.execute("search")
            papers = web_results['papers']
            
            # Extract figures from existing papers
            parse_results = self.parse_agent.execute(papers, "extract_figures")
            figures = parse_results['figures_extracted']
            
            # Generate content
            content_results = self.content_agent.execute(papers, figures, "full_content")
            categories = content_results['categories']
            
            # Validation
            if validate:
                validation_data = {
                    'papers': papers,
                    'categories': categories,
                    'figures': figures,
                    'content': {'html': content_results.get('research_html', '')}
                }
                validation_results = self.critic_agent.execute(validation_data, "full_validation")
            
            # Write only research and portfolio files
            file_results = self._write_research_files_only(content_results)
            
            pipeline_results['final_results'] = {
                'papers_processed': len(papers),
                'figures_extracted': len(figures),
                'categories_created': len(categories),
                'files_written': file_results.get('files_written', 0)
            }
            
            print("✅ Research-only update completed")
            return pipeline_results
            
        except Exception as e:
            pipeline_results['success'] = False
            pipeline_results['error'] = str(e)
            print(f"❌ Research update failed: {e}")
            return pipeline_results
    
    def _write_generated_files(self, content_results: Dict, papers: List[Dict]) -> Dict[str, Any]:
        """Write all generated files to disk."""
        file_results = {
            'success': True,
            'files_written': 0,
            'errors': []
        }
        
        try:
            # Write research.html
            if content_results.get('research_html'):
                try:
                    with open(config.research_page, 'w', encoding='utf-8') as f:
                        f.write(content_results['research_html'])
                    file_results['files_written'] += 1
                    print("   ✅ Research page updated")
                except Exception as e:
                    file_results['errors'].append(f"Research page: {e}")
            
            # Write portfolio pages
            if content_results.get('portfolio_pages'):
                for filename, content in content_results['portfolio_pages'].items():
                    try:
                        filepath = config.portfolio_dir / filename
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        file_results['files_written'] += 1
                        print(f"   ✅ Portfolio page: {filename}")
                    except Exception as e:
                        file_results['errors'].append(f"Portfolio {filename}: {e}")
            
            # Write publication files (if we have papers)
            if papers:
                pub_results = self._write_publication_files(papers)
                file_results['files_written'] += pub_results.get('written', 0)
                file_results['errors'].extend(pub_results.get('errors', []))
            
            if file_results['errors']:
                file_results['success'] = False
                for error in file_results['errors'][:3]:  # Show first 3 errors
                    print(f"   ⚠️ {error}")
            
            return file_results
            
        except Exception as e:
            file_results['success'] = False
            file_results['errors'].append(str(e))
            return file_results
    
    def _write_research_files_only(self, content_results: Dict) -> Dict[str, Any]:
        """Write only research and portfolio files."""
        file_results = {
            'success': True,
            'files_written': 0,
            'errors': []
        }
        
        try:
            # Clean existing portfolio files
            self._cleanup_portfolio_files()
            
            # Write research.html
            if content_results.get('research_html'):
                with open(config.research_page, 'w', encoding='utf-8') as f:
                    f.write(content_results['research_html'])
                file_results['files_written'] += 1
            
            # Write portfolio pages
            if content_results.get('portfolio_pages'):
                for filename, content in content_results['portfolio_pages'].items():
                    filepath = config.portfolio_dir / filename
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    file_results['files_written'] += 1
            
            return file_results
            
        except Exception as e:
            file_results['success'] = False
            file_results['errors'].append(str(e))
            return file_results
    
    def _write_publication_files(self, papers: List[Dict]) -> Dict[str, Any]:
        """Write publication markdown files."""
        results = {'written': 0, 'errors': []}
        
        # Sort papers by date (newest first)
        papers.sort(key=lambda x: self._format_date(x.get('date', '')), reverse=True)
        
        for paper in papers:
            try:
                title = paper['title']
                authors = ', '.join(paper.get('authors', []))
                pub_date = self._format_date(paper.get('date', ''))
                year = pub_date[:4]
                url_slug = self._create_url_slug(title)
                paper_url = paper.get('arxiv_url', '')
                venue = paper.get('venue', 'Preprint')
                
                excerpt = f'[<u><span style="color:blue">arXiv</span></u>]({paper_url})' if paper_url else ""
                citation = f"{authors} ({year}). \"{title}\". {venue}."
                
                filename = f"{pub_date}-{url_slug}.md"
                filepath = config.publications_dir / filename
                
                # Skip if file already exists
                if filepath.exists():
                    continue
                
                content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{url_slug}
excerpt: '{excerpt}'
date: {pub_date}
venue: '{venue}'
paperurl: '{paper_url}'
citation: '{self._clean_text(citation)}'
---

{paper.get('abstract', 'No abstract available.')}
"""
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                results['written'] += 1
                
            except Exception as e:
                results['errors'].append(f"Publication {paper.get('title', 'unknown')}: {e}")
        
        return results
    
    def _cleanup_portfolio_files(self):
        """Clean up existing portfolio files."""
        if config.portfolio_dir.exists():
            for file in config.portfolio_dir.glob("portfolio-*.md"):
                try:
                    file.unlink()
                except Exception:
                    pass
    
    def _format_date(self, date_str: str) -> str:
        """Format date for Jekyll."""
        if not date_str:
            return datetime.now().strftime('%Y-%m-%d')
        
        # Try different date patterns
        import re
        patterns = ['%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d', '%Y-%m', '%Y']
        
        for pattern in patterns:
            try:
                if pattern == '%Y-%m-%dT%H:%M:%SZ':
                    test_str = date_str[:19] + 'Z' if len(date_str) >= 19 else date_str
                else:
                    test_str = date_str[:len(pattern)]
                
                date_obj = datetime.strptime(test_str, pattern)
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                continue
        
        # Fallback: extract year
        year_match = re.search(r'(\d{4})', date_str)
        return f"{year_match.group(1)}-01-01" if year_match else datetime.now().strftime('%Y-%m-%d')
    
    def _create_url_slug(self, title: str) -> str:
        """Create URL-friendly slug."""
        import re
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        return re.sub(r'\s+', '-', slug)[:50]
    
    def _clean_text(self, text: str) -> str:
        """Clean text for YAML."""
        if not text:
            return ""
        import re
        text = re.sub(r'\s+', ' ', text.strip())
        return text.replace('"', '\\"')
    
    def _print_final_summary(self, results: Dict):
        """Print final summary of pipeline execution."""
        final = results['final_results']
        duration = results['duration'].total_seconds()
        
        print(f"📊 FINAL SUMMARY:")
        print(f"   Duration: {duration:.1f} seconds")
        print(f"   Papers processed: {final['papers_processed']}")
        print(f"   Figures extracted: {final['figures_extracted']}")
        print(f"   Categories created: {final['categories_created']}")
        print(f"   Files written: {final['files_written']}")
        print(f"   Validation: {'✅ PASSED' if final['validation_passed'] else '❌ ISSUES'}")

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Agentic Website Content Manager')
    parser.add_argument('--full-update', action='store_true',
                       help='Run complete website update (default)')
    parser.add_argument('--research-only', action='store_true',
                       help='Update only research and portfolio pages')
    parser.add_argument('--no-validation', action='store_true',
                       help='Skip validation checks')
    
    args = parser.parse_args()
    
    # Default to full update if no specific flags
    if not args.research_only:
        args.full_update = True
    
    try:
        orchestrator = WebsiteOrchestrator()
        
        validate = not args.no_validation
        
        if args.full_update:
            results = orchestrator.run_full_pipeline(validate=validate)
        elif args.research_only:
            results = orchestrator.run_research_only_update(validate=validate)
        
        # Exit with appropriate code
        sys.exit(0 if results['success'] else 1)
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Operation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()