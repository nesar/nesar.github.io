#!/usr/bin/env python3
"""
Improved publication updater for Nesar Ramachandra's academic website.
Combines arXiv and ADS (Astrophysics Data System) APIs for accurate publication data.
"""

import requests
import xml.etree.ElementTree as ET
import os
import re
import json
from datetime import datetime
import time

# Configuration
AUTHOR_NAME = "Ramachandra, Nesar"
AUTHOR_ORCID = None  # Add your ORCID if available
OUTPUT_DIR = "_publications"

def clean_text(text):
    """Clean and normalize text for YAML and markdown."""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Escape quotes for YAML
    text = text.replace('"', '\\"')
    
    return text

def create_url_slug(title):
    """Create a URL-friendly slug from title."""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    return slug[:50]  # Limit length

def get_arxiv_papers():
    """Fetch papers from arXiv API."""
    print("Fetching papers from arXiv...")
    
    # Try multiple search variations
    search_terms = [
        "au:\"Nesar S Ramachandra\"",
        "au:\"Ramachandra, Nesar\"", 
        "au:\"N S Ramachandra\"",
        "au:Ramachandra AND au:Nesar"
    ]
    
    all_papers = []
    
    for search_term in search_terms:
        url = f"http://export.arxiv.org/api/query?search_query={search_term}&sortBy=submittedDate&sortOrder=descending&max_results=100"
        print(f"Trying search: {search_term}")
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            root = ET.fromstring(response.content)
            namespace = {'atom': 'http://www.w3.org/2005/Atom'}
            
            papers_found = 0
            for entry in root.findall('.//atom:entry', namespace):
                # Extract basic info
                title = entry.find('./atom:title', namespace)
                published = entry.find('./atom:published', namespace)
                summary = entry.find('./atom:summary', namespace)
                arxiv_id = entry.find('./atom:id', namespace)
                
                if not all([title, published, arxiv_id]):
                    continue
                    
                title_text = clean_text(title.text)
                
                # Get authors and verify this is your paper
                authors = []
                for author in entry.findall('./atom:author', namespace):
                    name_elem = author.find('./atom:name', namespace)
                    if name_elem is not None:
                        authors.append(name_elem.text.strip())
                
                # Check if you're an author (multiple name formats)
                is_author = any(
                    ("Ramachandra" in author and "Nesar" in author) or
                    ("Ramachandra" in author and "N" in author) or
                    ("Nesar S" in author and "Ramachandra" in author)
                    for author in authors
                )
                
                if not is_author:
                    continue
                
                papers_found += 1
                
                # Extract arXiv ID for better linking
                arxiv_url = arxiv_id.text
                arxiv_match = re.search(r'(\d+\.\d+)', arxiv_url)
                arxiv_number = arxiv_match.group(1) if arxiv_match else ""
                
                # Look for DOI
                doi_url = ""
                for link in entry.findall('./atom:link', namespace):
                    if link.get('title') == 'doi':
                        doi_url = link.get('href')
                        break
                
                paper = {
                    'title': title_text,
                    'authors': authors,
                    'date': published.text,
                    'abstract': clean_text(summary.text if summary is not None else ""),
                    'arxiv_url': arxiv_url,
                    'arxiv_id': arxiv_number,
                    'doi_url': doi_url,
                    'venue': 'arXiv preprint',
                    'source': 'arxiv'
                }
                
                # Check if we already have this paper (by arXiv ID)
                if not any(p.get('arxiv_id') == arxiv_number for p in all_papers):
                    all_papers.append(paper)
            
            print(f"Found {papers_found} papers with search term: {search_term}")
            time.sleep(3)  # Be respectful to arXiv API
            
        except Exception as e:
            print(f"Error with search term '{search_term}': {e}")
            continue
            
    print(f"Found {len(all_papers)} total papers from arXiv")
    return all_papers

def get_ads_papers():
    """Fetch papers from NASA ADS API (if API key available)."""
    # Note: ADS requires an API key. For now, we'll skip this
    # You can get a free API key at https://ui.adsabs.harvard.edu/user/settings/token
    ads_token = os.environ.get('ADS_TOKEN')
    
    if not ads_token:
        print("ADS API token not found. Skipping ADS search.")
        return []
    
    print("Fetching papers from ADS...")
    
    headers = {
        'Authorization': f'Bearer {ads_token}',
        'Content-Type': 'application/json'
    }
    
    # Search query for your papers
    params = {
        'q': f'author:"Ramachandra, N" OR author:"Ramachandra, Nesar"',
        'fl': 'title,author,date,abstract,doi,bibcode,pub,citation_count',
        'rows': 200,
        'sort': 'date desc'
    }
    
    try:
        response = requests.get('https://api.adsabs.harvard.edu/v1/search/query', 
                              headers=headers, params=params, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        papers = []
        
        for doc in data.get('response', {}).get('docs', []):
            paper = {
                'title': clean_text(doc.get('title', [''])[0]),
                'authors': doc.get('author', []),
                'date': doc.get('date', ''),
                'abstract': clean_text(doc.get('abstract', '')),
                'doi_url': f"https://doi.org/{doc.get('doi', [''])[0]}" if doc.get('doi') else "",
                'ads_url': f"https://ui.adsabs.harvard.edu/abs/{doc.get('bibcode', '')}/abstract",
                'venue': doc.get('pub', 'Unknown'),
                'citation_count': doc.get('citation_count', 0),
                'source': 'ads'
            }
            papers.append(paper)
            
    except Exception as e:
        print(f"Error fetching from ADS: {e}")
        return []
    
    print(f"Found {len(papers)} papers from ADS")
    return papers

def merge_and_deduplicate_papers(arxiv_papers, ads_papers):
    """Merge and deduplicate papers from different sources."""
    all_papers = []
    seen_titles = set()
    
    # Priority: ADS (published) > arXiv (preprints)
    for paper in ads_papers + arxiv_papers:
        title_normalized = re.sub(r'\W+', '', paper['title'].lower())
        
        if title_normalized not in seen_titles:
            seen_titles.add(title_normalized)
            all_papers.append(paper)
    
    return all_papers

def format_date(date_str):
    """Format date for Jekyll."""
    if not date_str:
        return datetime.now().strftime('%Y-%m-%d')
    
    # Handle different date formats
    date_patterns = [
        '%Y-%m-%dT%H:%M:%SZ',  # arXiv format
        '%Y-%m-%d',            # Standard format
        '%Y-%m',               # Year-month only
        '%Y'                   # Year only
    ]
    
    for pattern in date_patterns:
        try:
            date_obj = datetime.strptime(date_str[:len(pattern)], pattern)
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            continue
    
    # Fallback: extract year if possible
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        return f"{year_match.group(1)}-01-01"
    
    return datetime.now().strftime('%Y-%m-%d')

def create_publication_file(paper, index):
    """Create a Jekyll markdown file for a publication."""
    title = paper['title']
    authors = paper.get('authors', [])
    
    # Format authors
    if isinstance(authors, list):
        authors_text = ', '.join(authors)
    else:
        authors_text = str(authors)
    
    # Format date
    pub_date = format_date(paper.get('date', ''))
    year = pub_date[:4]
    
    # Create URL slug
    url_slug = create_url_slug(title)
    
    # Determine best URL for paper
    paper_url = (paper.get('doi_url') or 
                paper.get('ads_url') or 
                paper.get('arxiv_url') or 
                "")
    
    # Create excerpt with appropriate link
    if paper.get('doi_url'):
        excerpt = f"[<u><span style='color:blue'>DOI</span></u>]({paper['doi_url']})"
    elif paper.get('ads_url'):
        excerpt = f"[<u><span style='color:blue'>ADS</span></u>]({paper['ads_url']})"
    elif paper.get('arxiv_url'):
        excerpt = f"[<u><span style='color:blue'>arXiv</span></u>]({paper['arxiv_url']})"
    else:
        excerpt = ""
    
    # Venue
    venue = paper.get('venue', 'Preprint')
    
    # Citation
    citation = f"{authors_text} ({year}). \"{title}\". {venue}."
    
    # Create filename
    filename = f"{pub_date}-{url_slug}.md"
    if os.path.exists(os.path.join(OUTPUT_DIR, filename)):
        filename = f"{pub_date}-{url_slug}-{index}.md"
    
    # Create content
    content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{url_slug}
excerpt: '{excerpt}'
date: {pub_date}
venue: '{venue}'
paperurl: '{paper_url}'
citation: '{clean_text(citation)}'
---

{paper.get('abstract', 'No abstract available.')}
"""
    
    # Write file
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created: {filename}")
        return True
    except Exception as e:
        print(f"Error creating {filename}: {e}")
        return False

def main():
    """Main function to update publications."""
    print("Starting publication update...")
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Clear existing files (optional - comment out to keep existing)
    # for file in os.listdir(OUTPUT_DIR):
    #     if file.endswith('.md'):
    #         os.remove(os.path.join(OUTPUT_DIR, file))
    
    # Fetch papers from sources
    arxiv_papers = get_arxiv_papers()
    ads_papers = get_ads_papers()
    
    # Merge and deduplicate
    all_papers = merge_and_deduplicate_papers(arxiv_papers, ads_papers)
    
    if not all_papers:
        print("No papers found!")
        return
    
    # Sort by date (newest first)
    all_papers.sort(key=lambda x: format_date(x.get('date', '')), reverse=True)
    
    # Create publication files
    successful = 0
    for i, paper in enumerate(all_papers):
        if create_publication_file(paper, i):
            successful += 1
        
        # Be respectful to APIs
        time.sleep(1)
    
    print(f"\nPublication update complete!")
    print(f"Successfully created {successful} out of {len(all_papers)} publication files.")
    
    if successful > 0:
        print("\nNext steps:")
        print("1. Review the generated files in _publications/")
        print("2. Run 'bundle exec jekyll serve' to test locally")
        print("3. Commit and push to GitHub to deploy")

if __name__ == "__main__":
    main()