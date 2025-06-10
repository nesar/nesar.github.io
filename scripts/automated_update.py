#!/usr/bin/env python3
"""
Automated update script for Nesar Ramachandra's academic website.
This script provides multiple automation options for updating publications and research.
"""

import os
import re
import json
import requests
from datetime import datetime
from typing import List, Dict
import argparse

class WebsiteUpdater:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.pub_dir = os.path.join(self.base_dir, "_publications")
        self.research_dir = os.path.join(self.base_dir, "_portfolio")
        
        # Ensure directories exist
        os.makedirs(self.pub_dir, exist_ok=True)
        os.makedirs(self.research_dir, exist_ok=True)
    
    def clean_text(self, text: str) -> str:
        """Clean text for YAML and markdown."""
        if not text:
            return ""
        text = re.sub(r'\s+', ' ', text.strip())
        text = text.replace('"', '\\"')
        return text
    
    def create_url_slug(self, title: str) -> str:
        """Create URL-friendly slug."""
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        return slug[:50]
    
    def format_date(self, date_str: str) -> str:
        """Format date for Jekyll."""
        if not date_str:
            return datetime.now().strftime('%Y-%m-%d')
        
        # Try different date formats
        formats = ['%Y-%m-%d', '%Y-%m', '%Y']
        for fmt in formats:
            try:
                if len(date_str) >= len(fmt):
                    date_obj = datetime.strptime(date_str[:len(fmt)], fmt)
                    return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                continue
        
        # Extract year if possible
        year_match = re.search(r'(\d{4})', date_str)
        if year_match:
            return f"{year_match.group(1)}-01-01"
        
        return datetime.now().strftime('%Y-%m-%d')
    
    def get_existing_publications(self) -> List[Dict]:
        """Get list of existing publications."""
        publications = []
        
        for filename in os.listdir(self.pub_dir):
            if not filename.endswith('.md'):
                continue
            
            try:
                with open(os.path.join(self.pub_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract YAML front matter
                yaml_match = re.search(r'---\s+(.*?)\s+---', content, re.DOTALL)
                if not yaml_match:
                    continue
                
                yaml_content = yaml_match.group(1)
                
                # Extract metadata
                title_match = re.search(r'title:\s*["\'](.*?)["\']', yaml_content, re.DOTALL)
                date_match = re.search(r'date:\s*([\d-]+)', yaml_content)
                venue_match = re.search(r'venue:\s*["\'](.*?)["\']', yaml_content)
                
                title = title_match.group(1) if title_match else "Unknown"
                date = date_match.group(1) if date_match else ""
                venue = venue_match.group(1) if venue_match else ""
                
                # Extract summary/abstract
                summary_match = re.search(r'---\s*\n\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
                summary = summary_match.group(1).strip() if summary_match else ""
                
                publications.append({
                    'filename': filename,
                    'title': title,
                    'date': date,
                    'venue': venue,
                    'summary': summary
                })
                
            except Exception as e:
                print(f"Error reading {filename}: {e}")
        
        return sorted(publications, key=lambda x: x['date'], reverse=True)
    
    def create_publication_file(self, pub_data: Dict, index: int = 0) -> bool:
        """Create a Jekyll publication file."""
        title = pub_data['title']
        date = self.format_date(pub_data.get('date', ''))
        year = date[:4]
        
        # Create URL slug
        url_slug = self.create_url_slug(title)
        
        # Create filename
        filename = f"{date}-{url_slug}.md"
        if os.path.exists(os.path.join(self.pub_dir, filename)):
            filename = f"{date}-{url_slug}-{index}.md"
        
        # Build content
        venue = pub_data.get('venue', 'Preprint')
        authors = pub_data.get('authors', '')
        paper_url = pub_data.get('url', '')
        abstract = pub_data.get('abstract', pub_data.get('summary', ''))
        
        # Create excerpt link
        if 'arxiv' in paper_url.lower():
            excerpt = f"[<u><span style='color:blue'>arXiv</span></u>]({paper_url})"
        elif 'doi.org' in paper_url:
            excerpt = f"[<u><span style='color:blue'>DOI</span></u>]({paper_url})"
        else:
            excerpt = f"[<u><span style='color:blue'>Link</span></u>]({paper_url})" if paper_url else ""
        
        citation = f"{authors} ({year}). \"{title}\". {venue}."
        
        content = f"""---
title: "{self.clean_text(title)}"
collection: publications
permalink: /publication/{year}-{url_slug}
excerpt: '{excerpt}'
date: {date}
venue: '{self.clean_text(venue)}'
paperurl: '{paper_url}'
citation: '{self.clean_text(citation)}'
---

{abstract}
"""
        
        try:
            with open(os.path.join(self.pub_dir, filename), 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created: {filename}")
            return True
        except Exception as e:
            print(f"Error creating {filename}: {e}")
            return False
    
    def update_research_from_publications(self):
        """Update research portfolio based on publications."""
        publications = self.get_existing_publications()
        
        # Group by research topics
        topics = {
            'machine-learning': {
                'title': 'Machine Learning & AI',
                'keywords': ['machine learning', 'deep learning', 'neural network', 'ai ', 'artificial intelligence', 'astromlab'],
                'papers': []
            },
            'dark-matter': {
                'title': 'Dark Matter & Cosmology',
                'keywords': ['dark matter', 'cosmic web', 'cosmology', 'halo', 'large scale structure'],
                'papers': []
            },
            'uncertainty-quantification': {
                'title': 'Uncertainty Quantification',
                'keywords': ['uncertainty', 'bayesian', 'probabilistic'],
                'papers': []
            },
            'gravitational-lensing': {
                'title': 'Gravitational Lensing',
                'keywords': ['gravitational lens', 'strong lens', 'weak lens', 'lensing'],
                'papers': []
            },
            'other-research': {
                'title': 'Other Research',
                'keywords': [],
                'papers': []
            }
        }
        
        # Categorize publications
        for pub in publications:
            text_to_search = (pub['title'] + ' ' + pub['summary']).lower()
            categorized = False
            
            for topic_key, topic_data in topics.items():
                if topic_key == 'other-research':
                    continue
                
                for keyword in topic_data['keywords']:
                    if keyword in text_to_search:
                        topic_data['papers'].append(pub)
                        categorized = True
                        break
                
                if categorized:
                    break
            
            if not categorized:
                topics['other-research']['papers'].append(pub)
        
        # Create portfolio files
        for i, (topic_key, topic_data) in enumerate(topics.items()):
            if not topic_data['papers']:
                continue
            
            filename = f"portfolio-{i+1}-{topic_key}.md"
            filepath = os.path.join(self.research_dir, filename)
            
            # Use first paper's summary as main description
            main_summary = topic_data['papers'][0]['summary'][:300] + "..." if topic_data['papers'] else ""
            
            content = f"""---
title: "{topic_data['title']}"
excerpt: "Research in {topic_data['title'].lower()} <br/><img src='/images/research_{topic_key}.png'>"
collection: portfolio
---

{main_summary}

## Related Publications ({len(topic_data['papers'])} papers):

"""
            
            for paper in topic_data['papers'][:10]:  # Limit to 10 most recent
                year = paper['date'][:4] if paper['date'] else ""
                content += f"- **{paper['title']}** ({year}) - {paper['venue']}\n"
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Created research file: {filename}")
            except Exception as e:
                print(f"Error creating research file {filename}: {e}")
    
    def add_publication_manually(self, title: str, authors: str, venue: str, 
                                 date: str, url: str = "", abstract: str = ""):
        """Add a publication manually."""
        pub_data = {
            'title': title,
            'authors': authors,
            'venue': venue,
            'date': date,
            'url': url,
            'abstract': abstract
        }
        
        return self.create_publication_file(pub_data)
    
    def clean_publications(self):
        """Remove duplicate or invalid publications."""
        publications = self.get_existing_publications()
        seen_titles = set()
        duplicates = []
        
        for pub in publications:
            title_norm = re.sub(r'\W+', '', pub['title'].lower())
            if title_norm in seen_titles:
                duplicates.append(pub['filename'])
            else:
                seen_titles.add(title_norm)
        
        for filename in duplicates:
            filepath = os.path.join(self.pub_dir, filename)
            print(f"Removing duplicate: {filename}")
            os.remove(filepath)
        
        print(f"Removed {len(duplicates)} duplicate publications")
    
    def list_publications(self):
        """List all current publications."""
        publications = self.get_existing_publications()
        
        print(f"\nCurrent Publications ({len(publications)} total):")
        print("=" * 60)
        
        for i, pub in enumerate(publications, 1):
            year = pub['date'][:4] if pub['date'] else "Unknown"
            print(f"{i:2d}. [{year}] {pub['title']}")
            print(f"    Venue: {pub['venue']}")
            print()

    def extract_figures_from_publications(self, max_papers: int = 3):
        """Extract figures from recent publications."""
        try:
            import subprocess
            result = subprocess.run(['python', 'scripts/auto_extract_from_publications.py'], 
                                  capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                print("✅ Figure extraction completed successfully")
                return True
            else:
                print(f"⚠️ Figure extraction completed with warnings:\n{result.stdout}")
                return True
        except Exception as e:
            print(f"❌ Error extracting figures: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Automated website updater')
    parser.add_argument('action', choices=[
        'list', 'clean', 'update-research', 'add-manual', 'extract-figures', 'full-update'
    ], help='Action to perform')
    
    parser.add_argument('--title', help='Publication title (for add-manual)')
    parser.add_argument('--authors', help='Authors (for add-manual)')
    parser.add_argument('--venue', help='Venue (for add-manual)')
    parser.add_argument('--date', help='Date YYYY-MM-DD (for add-manual)')
    parser.add_argument('--url', help='Paper URL (for add-manual)')
    parser.add_argument('--abstract', help='Abstract (for add-manual)')
    
    args = parser.parse_args()
    
    updater = WebsiteUpdater()
    
    if args.action == 'list':
        updater.list_publications()
    
    elif args.action == 'clean':
        updater.clean_publications()
    
    elif args.action == 'update-research':
        updater.update_research_from_publications()
    
    elif args.action == 'add-manual':
        if not all([args.title, args.authors, args.venue, args.date]):
            print("Error: --title, --authors, --venue, and --date are required for add-manual")
            return
        
        success = updater.add_publication_manually(
            args.title, args.authors, args.venue, args.date,
            args.url or "", args.abstract or ""
        )
        
        if success:
            print("Publication added successfully!")
        else:
            print("Failed to add publication.")
    
    elif args.action == 'extract-figures':
        updater.extract_figures_from_publications()
    
    elif args.action == 'full-update':
        print("🚀 Running full website update...")
        success_count = 0
        
        print("\n1. Cleaning duplicates...")
        updater.clean_publications()
        success_count += 1
        
        print("\n2. Updating research portfolio...")
        updater.update_research_from_publications()
        success_count += 1
        
        print("\n3. Extracting figures from papers...")
        if updater.extract_figures_from_publications():
            success_count += 1
        
        print(f"\n✅ Full update completed! ({success_count}/3 tasks successful)")
        print("\n💡 Next steps:")
        print("   1. Review the updated research pages")
        print("   2. Check extracted figures in images/research/figures/")
        print("   3. Test locally: bundle exec jekyll serve")
        print("   4. Commit and push changes")

if __name__ == "__main__":
    main()