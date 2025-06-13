#!/usr/bin/env python3
"""
Download YOUR actual papers from the _publications directory URLs.
This extracts the real paper URLs from your publication metadata.
"""

import os
import requests
import re
from pathlib import Path
import time

def extract_paper_urls():
    """Extract paper URLs from your _publications directory."""
    base_dir = Path(__file__).parent.parent
    publications_dir = base_dir / "_publications"
    papers_to_download = []
    
    # Focus on key papers from each research area
    target_papers = [
        # Foundation Models
        "astromlab-3-achieving-gpt-4o",
        "astromlab-1-who-wins",
        "astromlab-4-benchmark-topping",
        "eaira-establishing-a-methodology",
        
        # Machine Learning
        "modular-deep-learning-analysis",
        "anomaly-detection-in-astronomical",
        "generative-networks-for-emulating",
        "neural-network-based-point-spread",
        
        # Dark Matter & Cosmology
        "caustic-design-of-the-dark-matter",
        "topology-and-geometry-of-the-dark",
        "topology-geometry-and-morphology",
        
        # Emulation & Inference
        "probabilistic-neural-network-based",
        "probabilistic-neural-networks-for",
        "application-of-probabilistic-modeling"
    ]
    
    print(f"🔍 Scanning your publications for paper URLs...")
    
    for pub_file in publications_dir.glob("*.md"):
        try:
            with open(pub_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if this is one of our target papers
            filename = pub_file.stem.lower()
            is_target = any(target in filename for target in target_papers)
            
            if is_target:
                # Extract title
                title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content, re.MULTILINE)
                title = title_match.group(1) if title_match else filename
                
                # Extract arXiv URL from paperurl or excerpt
                arxiv_urls = []
                
                # Check paperurl field
                paperurl_match = re.search(r'paperurl:\s*["\']?([^"\'\\s]+)["\']?', content)
                if paperurl_match:
                    url = paperurl_match.group(1)
                    if 'arxiv.org' in url:
                        arxiv_urls.append(url)
                
                # Check excerpt for arXiv links
                excerpt_matches = re.findall(r'arxiv\.org/abs/([^)\\s]+)', content)
                for arxiv_id in excerpt_matches:
                    arxiv_urls.append(f"https://arxiv.org/abs/{arxiv_id}")
                
                # Convert to PDF URLs
                for arxiv_url in arxiv_urls:
                    if '/abs/' in arxiv_url:
                        pdf_url = arxiv_url.replace('/abs/', '/pdf/') + '.pdf'
                        
                        # Create safe filename
                        safe_title = re.sub(r'[^\w\s-]', '', title)
                        safe_title = re.sub(r'\s+', '_', safe_title)
                        filename = f"{safe_title[:50]}.pdf"
                        
                        papers_to_download.append({
                            'url': pdf_url,
                            'filename': filename,
                            'title': title,
                            'source_file': pub_file.name
                        })
                        break  # Only need one URL per paper
        
        except Exception as e:
            print(f"⚠️ Error processing {pub_file.name}: {e}")
            continue
    
    return papers_to_download

def download_paper(paper_info):
    """Download a single paper."""
    try:
        print(f"📥 Downloading: {paper_info['title'][:50]}...")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(paper_info['url'], headers=headers, stream=True, timeout=60)
        response.raise_for_status()
        
        base_dir = Path(__file__).parent.parent
        papers_dir = base_dir / "temp_papers"
        papers_dir.mkdir(exist_ok=True)
        
        filepath = papers_dir / paper_info['filename']
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"   ✅ Saved as: {paper_info['filename']} ({os.path.getsize(filepath)} bytes)")
        return str(filepath)
        
    except Exception as e:
        print(f"   ❌ Error downloading {paper_info['filename']}: {e}")
        return None

def main():
    """Download your actual papers."""
    
    # Clear any existing random papers
    base_dir = Path(__file__).parent.parent
    papers_dir = base_dir / "temp_papers"
    if papers_dir.exists():
        for file in papers_dir.glob("*.pdf"):
            if file.name not in ["a_modular_deep_learning_pipeline_for_galaxy-scale_.pdf"]:  # Keep one that was working
                file.unlink()
    
    papers_to_download = extract_paper_urls()
    
    if not papers_to_download:
        print("❌ No downloadable papers found in your publications")
        return
    
    print(f"🚀 Found {len(papers_to_download)} of YOUR papers to download...")
    
    downloaded = []
    for paper_info in papers_to_download[:8]:  # Limit to 8 papers to avoid overwhelming arXiv
        filepath = download_paper(paper_info)
        if filepath:
            downloaded.append(filepath)
        time.sleep(2)  # Be respectful to arXiv servers
    
    print(f"\n📊 Successfully downloaded {len(downloaded)} of YOUR papers!")
    
    if downloaded:
        print("\n📋 Downloaded papers:")
        for paper_info in papers_to_download[:len(downloaded)]:
            print(f"   - {paper_info['title'][:60]}")
        
        print(f"\n🔍 Now run: python scripts/advanced_figure_extractor.py")
        print("   to extract figures from YOUR actual papers")

if __name__ == "__main__":
    main()