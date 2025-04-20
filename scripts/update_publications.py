#!/usr/bin/env python3
"""
Script to automatically update publications from arXiv and ADS.
This script fetches publications for a specific author and creates/updates
the corresponding markdown files in the _publications directory.
"""

import os
import re
import time
import requests
import yaml
from datetime import datetime

# Configuration
AUTHOR_NAME = "Ramachandra, Nesar"  # Your name as it appears in publications
ARXIV_SEARCH_QUERY = "au:Ramachandra_N"  # arXiv search query for your papers
ADS_API_TOKEN = os.environ.get("ADS_API_TOKEN", "20ugit1lLsoATYZO9FCTGvBUvbCx3HgLn2Z8AHYR")  # Your ADS API token
PUBLICATIONS_DIR = "_publications"

def clean_title(title):
    """Clean a title to use as part of a filename."""
    title = re.sub(r'[^\w\s-]', '', title.lower())
    title = re.sub(r'[\s]+', '-', title)
    return title[:50]  # Limit length

def fetch_from_arxiv():
    """Fetch publications from arXiv API."""
    url = f"http://export.arxiv.org/api/query?search_query={ARXIV_SEARCH_QUERY}&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching from arXiv: {response.status_code}")
        return []
    
    # Parse arXiv XML response
    from xml.etree import ElementTree
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ElementTree.fromstring(response.text)
    
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

def fetch_from_ads():
    """Fetch publications from NASA ADS API."""
    if not ADS_API_TOKEN:
        print("No ADS API token provided, skipping ADS fetch")
        return []
    
    headers = {"Authorization": f"Bearer {ADS_API_TOKEN}"}
    params = {
        "q": f"author:\"{AUTHOR_NAME}\"",
        "fl": "title,author,abstract,bibcode,pub,volume,issue,year,doi",
        "sort": "date desc",
        "rows": 100
    }
    
    url = "https://api.adsabs.harvard.edu/v1/search/query"
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching from ADS: {response.status_code}")
        return []
    
    papers = []
    data = response.json()
    
    for paper in data.get("response", {}).get("docs", []):
        title = paper.get("title", ["Untitled"])[0]
        authors = paper.get("author", [])
        year = paper.get("year", "")
        pub_date = f"{year}-01-01"  # Default to January 1st of the year
        
        papers.append({
            "title": title,
            "authors": authors,
            "pub_date": pub_date,
            "abstract": paper.get("abstract", ""),
            "doi": paper.get("doi", [""])[0] if paper.get("doi") else "",
            "venue": paper.get("pub", ""),
            "volume": paper.get("volume", ""),
            "issue": paper.get("issue", ""),
            "year": year,
            "bibcode": paper.get("bibcode", "")
        })
    
    return papers

def create_publication_file(paper, source="arxiv"):
    """Create or update a publication markdown file."""
    # Generate filename
    title_slug = clean_title(paper["title"])
    year = paper["pub_date"].split("-")[0]
    filename = f"{year}Ramachandra_{len(os.listdir(PUBLICATIONS_DIR)) % 10}.md"
    filepath = os.path.join(PUBLICATIONS_DIR, filename)
    
    # Check if file already exists
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
            # If it's the same paper (check by title), skip it
            if paper["title"] in content:
                print(f"Publication already exists: {filename}")
                return
    
    # Format authors with bold for your name
    authors = []
    for author in paper.get("authors", []):
        if "Ramachandra" in author and "Nesar" in author:
            authors.append(f"<b> {author} </b>")
        else:
            authors.append(author)
            
    authors_str = ", ".join(authors)
    
    # Create front matter
    front_matter = {
        "title": paper["title"],
        "collection": "publications",
        "permalink": f"/publication/{year}Ramachandra_{len(os.listdir(PUBLICATIONS_DIR)) % 10}",
        "excerpt": f'[<u><span style="color:blue"> arXiv link </span></u>]({paper.get("arxiv_url", "")})',
        "date": paper["pub_date"],
        "venue": paper.get("venue", "arXiv preprint"),
    }
    
    if source == "arxiv" and paper.get("arxiv_url"):
        front_matter["paperurl"] = paper["arxiv_url"]
    elif source == "ads" and paper.get("doi"):
        front_matter["paperurl"] = f"https://doi.org/{paper['doi']}"
    
    # Format citation
    if source == "arxiv":
        front_matter["citation"] = f"{authors_str}; {paper['title']}, arXiv:{paper.get('arxiv_id', '')}"
    else:  # ADS
        venue_details = []
        if paper.get("venue"):
            venue_details.append(paper["venue"])
        if paper.get("volume"):
            venue_details.append(f"Volume {paper['volume']}")
        if paper.get("issue"):
            venue_details.append(f"Issue {paper['issue']}")
        if paper.get("year"):
            venue_details.append(paper["year"])
        
        venue_str = ", ".join(venue_details)
        front_matter["citation"] = f"{authors_str}; {paper['title']}, {venue_str}"
    
    # Write to file
    with open(filepath, 'w') as f:
        # Write YAML front matter
        f.write("---\n")
        for key, value in front_matter.items():
            f.write(f"{key}: \"{value}\"\n")
        f.write("---\n\n\n")
        
        # Write summary
        f.write(f"Summary: {paper['abstract'][:500]}...")
    
    print(f"Created publication file: {filename}")

def main():
    """Main function to update publications."""
    # Create publications directory if it doesn't exist
    os.makedirs(PUBLICATIONS_DIR, exist_ok=True)
    
    # Fetch publications from arXiv
    arxiv_papers = fetch_from_arxiv()
    for paper in arxiv_papers:
        create_publication_file(paper, source="arxiv")
        time.sleep(1)  # Be nice to the API
    
    # Fetch publications from ADS
    ads_papers = fetch_from_ads()
    for paper in ads_papers:
        # Avoid duplicates from arXiv
        if not any(ap["title"] == paper["title"] for ap in arxiv_papers):
            create_publication_file(paper, source="ads")
            time.sleep(1)  # Be nice to the API
    
    print(f"Total publications processed: {len(arxiv_papers) + len(ads_papers)}")

if __name__ == "__main__":
    main()
