#!/usr/bin/env python3
"""
Simple script to fetch recent publications from arXiv.
"""

import os
import requests
import xml.etree.ElementTree as ET
import re
from datetime import datetime

# Configuration
AUTHOR_NAME = "Ramachandra, N"  # Your name as it appears in publications
ARXIV_SEARCH_QUERY = "au:Ramachandra_N"  # arXiv search query for your papers
PUBLICATIONS_DIR = "_publications"

def clean_title(title):
    """Clean a title to use as part of a filename."""
    title = re.sub(r'[^\w\s-]', '', title.lower())
    title = re.sub(r'[\s]+', '-', title)
    return title[:50]  # Limit length

def fetch_from_arxiv():
    """Fetch publications from arXiv API."""
    url = f"http://export.arxiv.org/api/query?search_query={ARXIV_SEARCH_QUERY}&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching from arXiv: {response.status_code}")
        return []
    
    # Parse arXiv XML response
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(response.text)
    
    papers = []
    for entry in root.findall(".//atom:entry", ns):
        title_elem = entry.find("atom:title", ns)
        title = title_elem.text.strip() if title_elem is not None else "Untitled"
        
        # Skip entries that don't have your name in the authors
        authors_elem = entry.find("atom:author/atom:name", ns)
        if authors_elem is None or AUTHOR_NAME.lower() not in authors_elem.text.lower():
            continue
        
        # Get all authors
        all_authors = []
        for author in entry.findall(".//atom:author/atom:name", ns):
            all_authors.append(author.text.strip())
        
        # Format date
        published = entry.find("atom:published", ns)
        if published is not None:
            pub_date = published.text[:10]  # YYYY-MM-DD format
        else:
            pub_date = datetime.now().strftime("%Y-%m-%d")
        
        # Get abstract
        summary = entry.find("atom:summary", ns)
        abstract = summary.text.strip() if summary is not None else ""
        
        # Get arXiv link and ID
        arxiv_url = None
        arxiv_id = None
        for link in entry.findall("atom:link", ns):
            href = link.get("href", "")
            if "arxiv.org/abs/" in href:
                arxiv_url = href
                arxiv_id = href.split("/")[-1]
                break
        
        papers.append({
            "title": title,
            "authors": all_authors,
            "pub_date": pub_date,
            "abstract": abstract,
            "arxiv_url": arxiv_url,
            "arxiv_id": arxiv_id
        })
    
    return papers

def create_publication_file(paper):
    """Create a publication markdown file."""
    # Generate filename
    year = paper["pub_date"].split("-")[0]
    index = len(os.listdir(PUBLICATIONS_DIR)) % 10
    filename = f"{year}Ramachandra_{index}.md"
    filepath = os.path.join(PUBLICATIONS_DIR, filename)
    
    # Check if file already exists - simple check by title
    for existing_file in os.listdir(PUBLICATIONS_DIR):
        if existing_file.startswith(year):
            with open(os.path.join(PUBLICATIONS_DIR, existing_file), 'r') as f:
                content = f.read()
                if paper["title"] in content:
                    print(f"Publication already exists: {paper['title']}")
                    return
    
    # Format authors with bold for your name
    authors = []
    for author in paper.get("authors", []):
        if "Ramachandra" in author and "Nesar" in author:
            authors.append(f"<b> {author} </b>")
        else:
            authors.append(author)
            
    authors_str = ", ".join(authors)
    
    # Create content
    content = f"""---
title: "{paper['title']}"
collection: publications
permalink: /publication/{year}Ramachandra_{index}
excerpt: '[<u><span style="color:blue"> arXiv link </span></u>]({paper.get("arxiv_url", "")})'
date: {paper['pub_date']}
venue: 'arXiv preprint'
paperurl: '{paper.get("arxiv_url", "")}'
citation: '{authors_str}; {paper["title"]}, arXiv:{paper.get("arxiv_id", "")}'
---


Summary: {paper['abstract'][:500]}...
"""
    
    # Write to file
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Created publication file: {filename}")

def main():
    """Main function to update publications."""
    if not os.path.exists(PUBLICATIONS_DIR):
        print(f"Creating directory: {PUBLICATIONS_DIR}")
        os.makedirs(PUBLICATIONS_DIR)
    
    # Fetch publications from arXiv
    print("Fetching publications from arXiv...")
    arxiv_papers = fetch_from_arxiv()
    
    # Create publication files
    for paper in arxiv_papers:
        create_publication_file(paper)
    
    print(f"Total publications processed: {len(arxiv_papers)}")

if __name__ == "__main__":
    main()
