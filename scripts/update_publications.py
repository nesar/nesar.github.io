#!/usr/bin/env python3
import requests
import xml.etree.ElementTree as ET
import os
import re
from datetime import datetime

# Function to clean HTML tags
def clean_html(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Function to format date
def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    return date_obj.strftime('%Y-%m-%d')

# Set the author name to search for
author_name = "Ramachandra, Nesar"

# Create the arXiv API query URL
url = f"http://export.arxiv.org/api/query?search_query=au:{author_name}&sortBy=submittedDate&sortOrder=descending&max_results=100"

# Make the API request
response = requests.get(url)
root = ET.fromstring(response.content)

# Create directory for publications if it doesn't exist
os.makedirs("_publications", exist_ok=True)

# Define the namespace used in arXiv API
namespace = {'atom': 'http://www.w3.org/2005/Atom'}

# Loop through each entry (paper)
for entry in root.findall('.//atom:entry', namespace):
    # Extract paper details
    title = entry.find('./atom:title', namespace).text.strip()
    published = entry.find('./atom:published', namespace).text
    summary = entry.find('./atom:summary', namespace).text.strip()
    arxiv_link = entry.find('./atom:id', namespace).text
    
    # Format the date for Jekyll
    pub_date = format_date(published)
    
    # Create a URL slug from the title
    url_slug = title.lower().replace(' ', '-')
    url_slug = re.sub(r'[^a-z0-9-]', '', url_slug)
    
    # Year for the permalink and citation
    year = pub_date[:4]
    
    # Get all authors and verify this is your paper
    all_authors = []
    for author in entry.findall('./atom:author', namespace):
        author_name_elem = author.find('./atom:name', namespace)
        if author_name_elem is not None:
            all_authors.append(author_name_elem.text)
    
    authors_text = "; ".join(all_authors)
    
    # Skip if your name is not in the author list
    if not any("Ramachandra" in author and "Nesar" in author for author in all_authors):
        print(f"Skipping paper not authored by you: {title}")
        continue
    
    # Get DOI and journal information if available
    journal_ref = "Preprint"
    doi_link = ""
    
    for link in entry.findall('./atom:link', namespace):
        if link.get('title') == 'doi':
            doi_link = link.get('href')
    
    # Create the filename
    filename = f"{pub_date}-{url_slug}.md"
    file_path = os.path.join("_publications", filename)
    
    # Create the markdown content
    content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}{url_slug}
excerpt: '[<u><span style="color:blue"> arXiv link </span></u>]({arxiv_link})'
date: {pub_date}
venue: '{journal_ref}'
paperurl: '{doi_link if doi_link else arxiv_link}'
citation: '{authors_text}; {title}, {journal_ref}'
---


Summary: {summary}
"""
    
    # Write the markdown file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created publication file: {filename}")

print("Publication update complete!")
