#!/usr/bin/env python3
import os
import re
from scholarly import scholarly
import time
from datetime import datetime

# Create directory for publications if it doesn't exist
os.makedirs("_publications", exist_ok=True)

# Function to clean text for YAML
def clean_for_yaml(text):
    if text is None:
        return ""
    # Replace quotes with escaped quotes
    text = text.replace('"', '\\"')
    return text

# Function to create a URL slug
def create_slug(title):
    # Convert to lowercase and replace spaces with hyphens
    slug = title.lower().replace(' ', '-')
    # Remove any non-alphanumeric characters (except hyphens)
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # Limit length
    if len(slug) > 50:
        slug = slug[:50]
    return slug

# Search for author profile
print("Searching for author profile...")
author_query = scholarly.search_author('Nesar Ramachandra')
author = next(author_query)

# Fill in author details
print(f"Found author: {author['name']}")
author = scholarly.fill(author)

# Get publications
publications = author['publications']
print(f"Found {len(publications)} publications")

# Create a counter for successful file creations
successful_files = 0

# Process each publication
for i, pub in enumerate(publications):
    try:
        # Get basic publication info first 
        title = clean_for_yaml(pub.get('bib', {}).get('title', 'Unknown title'))
        print(f"Processing publication {i+1}/{len(publications)}: {title}")
        
        # Try to get detailed info, but continue even if it fails
        try:
            pub_filled = scholarly.fill(pub)
        except Exception as e:
            print(f"Warning: Could not get full details for {title}: {e}")
            pub_filled = pub  # Use the basic info instead
        
        # Extract publication details
        title = clean_for_yaml(pub_filled.get('bib', {}).get('title', 'Unknown title'))
        venue = clean_for_yaml(pub_filled.get('bib', {}).get('journal', pub_filled.get('bib', {}).get('venue', 'Preprint')))
        year = pub_filled.get('bib', {}).get('pub_year', datetime.now().year)
        
        # Format date - use Jan 1st if only year is available
        if isinstance(year, int) or re.match(r'^\d{4}$', str(year)):
            pub_date = f"{year}-01-01"
        else:
            # Use current date if year is not available
            pub_date = datetime.now().strftime('%Y-%m-%d')
        
        # Generate URL slug from title
        url_slug = create_slug(title)
        
        # Get authors
        authors = pub_filled.get('bib', {}).get('author', 'Unknown authors')
        if isinstance(authors, list):
            authors = ', '.join(authors)
        
        # Get abstract
        abstract = pub_filled.get('bib', {}).get('abstract', 'No abstract available')
        
        # Get URLs - fallback chain
        pub_url = ''
        for url_key in ['pub_url', 'url_pdf', 'eprint']:
            if url_key in pub_filled and pub_filled[url_key]:
                pub_url = pub_filled[url_key]
                break
        
        # Get scholar URL - even if cluster_id is missing
        scholar_url = ""
        if 'cluster_id' in pub_filled:
            scholar_url = f"https://scholar.google.com/scholar?cluster={pub_filled['cluster_id']}"
        else:
            # Create a search URL based on the title
            scholar_url = f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"
        
        # Determine citation format
        citation = f"{authors} ({year}). \"{title}\". {venue}."
        
        # Create the filename - add index to ensure uniqueness
        filename = f"{pub_date}-{url_slug}-{i}.md"
        file_path = os.path.join("_publications", filename)
        
        # Create the markdown content
        content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{url_slug}
excerpt: '[<u><span style="color:blue">Google Scholar</span></u>]({scholar_url})'
date: {pub_date}
venue: '{venue}'
paperurl: '{pub_url if pub_url else scholar_url}'
citation: '{citation}'
---

Summary: {abstract}
"""
        
        # Write the markdown file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created publication file: {filename}")
        successful_files += 1
        
        # Sleep briefly to avoid hitting rate limits
        time.sleep(2)
        
    except Exception as e:
        print(f"Error processing publication {i+1}: {e}")

print(f"Publication update complete! Successfully created {successful_files} out of {len(publications)} files.")
