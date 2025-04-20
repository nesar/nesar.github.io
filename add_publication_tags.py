#!/usr/bin/env python3
"""
Script to add tags to publication files based on content.
These tags help with filtering on the publications page.
"""

import os
import re
import glob
import yaml
import frontmatter

# Configuration
PUBLICATIONS_DIR = "_publications"

# Define tag keywords
TAG_KEYWORDS = {
    "cosmic_web": ["cosmic web", "dark matter", "filament", "void", "structure", 
                  "multistream", "halo", "topology", "geometry", "cosmology"],
    "machine_learning": ["machine learning", "deep learning", "neural network", 
                        "ai", "cnn", "convolutional", "predictive model", 
                        "classification", "regression", "pytorch", "tensorflow"],
    "gravitational_lensing": ["gravitational lens", "strong lensing", "weak lensing", 
                            "lensing system", "lens modeling"],
    "uncertainty_quantification": ["uncertainty", "bayesian", "probabilistic", 
                                 "error estimation", "confidence interval"]
}

def get_tags_from_content(text):
    """Extract tags based on keywords in the text."""
    text = text.lower()
    tags = set()
    
    for category, keywords in TAG_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in text:
                # Add both the category and specific keyword as tags
                tags.add(category.replace("_", "-"))
                tags.add(keyword.replace(" ", "-").replace("_", "-"))
                break
    
    return list(tags)

def update_publication_tags():
    """Find and update tags in all publication files."""
    publication_files = glob.glob(os.path.join(PUBLICATIONS_DIR, "*.md"))
    
    for filepath in publication_files:
        try:
            # Read the file with python-frontmatter
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # Extract text from title, excerpt, and content
            title = post.get('title', '')
            excerpt = post.get('excerpt', '')
            content = post.content
            
            all_text = f"{title} {excerpt} {content}"
            
            # Get tags
            tags = get_tags_from_content(all_text)
            
            # Add tags to frontmatter if new tags were found
            existing_tags = post.get('tags', [])
            if not existing_tags:
                existing_tags = []
            
            # Combine existing and new tags
            combined_tags = list(set(existing_tags + tags))
            
            if combined_tags != existing_tags:
                post['tags'] = combined_tags
                
                # Write the updated file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(frontmatter.dumps(post))
                
                print(f"Updated tags for {os.path.basename(filepath)}: {combined_tags}")
            else:
                print(f"No new tags for {os.path.basename(filepath)}")
        
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    update_publication_tags()
