#!/usr/bin/env python3
import os
import re
import yaml
from collections import defaultdict

# Function to extract topics from paper summaries
def extract_topics(summary):
    # List of keywords to look for
    topics = {
        "dark matter": ["dark matter", "dm ", "halo", "cosmic web"],
        "machine learning": ["machine learning", "deep learning", "neural network", "ai ", "artificial intelligence"],
        "cosmology": ["cosmology", "cosmological", "universe", "lsst", "large scale structure"],
        "gravitational lensing": ["gravitational lens", "strong lens", "weak lens"],
        "uncertainty quantification": ["uncertainty", "bayesian", "probabilistic"],
    }
    
    found_topics = set()
    summary_lower = summary.lower()
    
    for topic, keywords in topics.items():
        for keyword in keywords:
            if keyword in summary_lower:
                found_topics.add(topic)
                break
    
    return list(found_topics)

# Dictionary to store research by topic
research_by_topic = defaultdict(list)

# Process all publication files
pub_dir = "_publications"
for filename in os.listdir(pub_dir):
    if not filename.endswith(".md"):
        continue
    
    try:
        with open(os.path.join(pub_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML front matter using regex
        yaml_match = re.search(r'---\s+(.*?)\s+---', content, re.DOTALL)
        if not yaml_match:
            print(f"Warning: Could not extract YAML front matter from {filename}")
            continue
        
        yaml_content = yaml_match.group(1)
        
        # Extract metadata manually with regex instead of yaml parser
        title_match = re.search(r'title:\s*["\'](.*?)["\']', yaml_content, re.DOTALL)
        title = title_match.group(1) if title_match else "Untitled"
        
        date_match = re.search(r'date:\s*([\d-]+)', yaml_content)
        date = date_match.group(1) if date_match else ""
        
        permalink_match = re.search(r'permalink:\s*(.*?)$', yaml_content, re.MULTILINE)
        permalink = permalink_match.group(1).strip() if permalink_match else ""
        
        # Extract summary
        summary_match = re.search(r'Summary:(.*?)(?=\n\n|\Z)', content, re.DOTALL)
        summary = summary_match.group(1).strip() if summary_match else ""
        
        # Extract topics
        topics = extract_topics(summary)
        
        # If no topics found, add to "Other"
        if not topics:
            topics = ["Other Research"]
        
        # Add to research dictionary
        for topic in topics:
            research_by_topic[topic].append({
                "title": title,
                "date": date,
                "summary": summary[:200] + "..." if len(summary) > 200 else summary,
                "url": permalink
            })
        
        print(f"Processed: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Create research portfolio files
os.makedirs("_portfolio", exist_ok=True)

# Sort topics by number of papers (descending)
sorted_topics = sorted(research_by_topic.keys(), 
                       key=lambda x: len(research_by_topic[x]), 
                       reverse=True)

for i, topic in enumerate(sorted_topics):
    papers = research_by_topic[topic]
    
    # Sort papers by date (newest first)
    papers.sort(key=lambda x: x["date"], reverse=True)
    
    filename = f"portfolio-{i+1}-{topic.lower().replace(' ', '-')}.md"
    file_path = os.path.join("_portfolio", filename)
    
    # Create image path (you'd need to create these images)
    image_name = topic.lower().replace(" ", "_") + ".png"
    
    # Create a fallback image if topic-specific one doesn't exist
    if not os.path.exists(os.path.join("images", image_name)):
        image_name = "research_default.png"
    
    content = f"""---
title: "{topic.title()}"
excerpt: "Research on {topic} <br/><img src='/images/{image_name}'>"
collection: research
---

{papers[0]["summary"] if papers else ""}

## Related Papers:

{{% include base_path %}}

"""
    
    for paper in papers:
        content += f"- [{paper['title']}]({paper['url']})\n"
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created research file: {filename}")
    except Exception as e:
        print(f"Error creating {filename}: {e}")

print("Research update complete!")
