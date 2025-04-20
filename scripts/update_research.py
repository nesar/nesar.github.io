#!/usr/bin/env python3
"""
Script to automatically update research portfolio based on publications.
This script analyzes publication content to extract research themes and
generates/updates portfolio items in the _portfolio directory.
"""

import os
import re
import yaml
import glob
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Configuration
PUBLICATIONS_DIR = "_publications"
PORTFOLIO_DIR = "_portfolio"
RESEARCH_THEMES = {
    "cosmic_web": ["cosmic web", "dark matter", "filament", "void", "structure", "multistream", "halo", "topology", "geometry"],
    "machine_learning": ["machine learning", "deep learning", "neural network", "ai", "cnn", "predictive model", "classification", "regression"],
    "gravitational_lensing": ["gravitational lens", "strong lensing", "weak lensing", "lensing system"],
    "uncertainty_quantification": ["uncertainty", "bayesian", "probabilistic", "error estimation"]
}

def extract_text_from_publication(filepath):
    """Extract text content from a publication markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract title and abstract
    title_match = re.search(r'title: "([^"]+)"', content)
    title = title_match.group(1) if title_match else ""
    
    # Extract the summary section
    summary_match = re.search(r'Summary: (.*?)(?:\.{3}|\Z)', content, re.DOTALL)
    summary = summary_match.group(1).strip() if summary_match else ""
    
    return {
        "title": title,
        "text": f"{title}. {summary}",
        "filepath": filepath
    }

def classify_publications_by_theme():
    """Classify publications into research themes."""
    publications = []
    for filepath in glob.glob(os.path.join(PUBLICATIONS_DIR, "*.md")):
        pub_data = extract_text_from_publication(filepath)
        if pub_data["text"]:
            publications.append(pub_data)
    
    # Classify each publication by theme
    theme_publications = defaultdict(list)
    
    for pub in publications:
        text = pub["text"].lower()
        max_score = 0
        best_theme = "other"
        
        for theme, keywords in RESEARCH_THEMES.items():
            score = sum(1 for keyword in keywords if keyword.lower() in text)
            if score > max_score:
                max_score = score
                best_theme = theme
        
        theme_publications[best_theme].append(pub)
    
    return theme_publications

def extract_key_phrases(texts, n=5):
    """Extract key phrases from a collection of texts."""
    if not texts:
        return []
    
    # Combine texts
    combined_text = " ".join(texts)
    
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(combined_text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Get word frequencies
    word_freq = defaultdict(int)
    for word in filtered_words:
        word_freq[word] += 1
    
    # Return top N phrases
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:n]

def generate_portfolio_item(theme, publications):
    """Generate a portfolio item for a research theme."""
    if not publications:
        return
    
    # Theme name formatting
    theme_title = " ".join(word.capitalize() for word in theme.split("_"))
    theme_slug = theme.lower()
    
    # Extract titles and texts
    titles = [pub["title"] for pub in publications]
    texts = [pub["text"] for pub in publications]
    
    # Get key phrases
    key_phrases = extract_key_phrases(texts)
    key_phrases_text = ", ".join([phrase for phrase, _ in key_phrases])
    
    # Generate short description
    description = f"Research on {theme_title} including topics such as {key_phrases_text}."
    
    # Create portfolio file
    filename = f"{theme_slug}.md"
    filepath = os.path.join(PORTFOLIO_DIR, filename)
    
    frontmatter = {
        "title": theme_title,
        "excerpt": f"{description} <br/><img src='/images/{theme_slug}.png'>",
        "collection": "portfolio"
    }
    
    content = f"""---
title: "{frontmatter['title']}"
excerpt: "{frontmatter['excerpt']}"
collection: portfolio
---

{description}

## Related Publications

"""
    
    # Add related publications
    for pub in publications:
        title = pub["title"]
        filepath = pub["filepath"]
        
        # Extract permalink from publication
        with open(filepath, 'r') as f:
            pub_content = f.read()
        
        permalink_match = re.search(r'permalink: ([^\n]+)', pub_content)
        permalink = permalink_match.group(1) if permalink_match else ""
        
        if permalink:
            content += f"- [{title}]({permalink})\n"
        else:
            content += f"- {title}\n"
    
    # Write to file
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Created portfolio item: {filename}")

def main():
    """Main function to update research portfolio."""
    # Create portfolio directory if it doesn't exist
    os.makedirs(PORTFOLIO_DIR, exist_ok=True)
    
    # Classify publications by theme
    theme_publications = classify_publications_by_theme()
    
    # Generate portfolio items
    for theme, publications in theme_publications.items():
        generate_portfolio_item(theme, publications)
    
    print(f"Total research themes processed: {len(theme_publications)}")

if __name__ == "__main__":
    main()
