#!/usr/bin/env python3
"""
Download Foundation Models papers that should have extractable figures.
"""

import requests
import os
from pathlib import Path
import time

def download_paper(url, filename):
    """Download a paper from URL."""
    try:
        print(f"📥 Downloading {filename}...")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, stream=True, timeout=60)
        response.raise_for_status()
        
        base_dir = Path(__file__).parent.parent
        papers_dir = base_dir / "temp_papers"
        papers_dir.mkdir(exist_ok=True)
        
        filepath = papers_dir / filename
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Downloaded {filename} ({os.path.getsize(filepath)} bytes)")
        return str(filepath)
        
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")
        return None

def main():
    """Download Foundation Models papers."""
    
    # Papers that should have good figures
    papers = [
        {
            'url': 'https://arxiv.org/pdf/2410.07746.pdf',  # AstroMLab-1
            'filename': 'astromlab_1_who_wins_astronomy_jeopardy.pdf'
        },
        {
            'url': 'https://arxiv.org/pdf/2411.17804.pdf',  # AstroMLab-3 
            'filename': 'astromlab_3_achieving_gpt4o_level_performance.pdf'
        },
        {
            'url': 'https://arxiv.org/pdf/2405.01104.pdf',  # EAIRA
            'filename': 'eaira_establishing_ai_methodology.pdf'
        }
    ]
    
    print(f"🚀 Downloading {len(papers)} Foundation Models papers...")
    
    downloaded = []
    for paper in papers:
        filepath = download_paper(paper['url'], paper['filename'])
        if filepath:
            downloaded.append(filepath)
        time.sleep(1)  # Be nice to servers
    
    print(f"\n📊 Downloaded {len(downloaded)} papers successfully")
    
    if downloaded:
        print("\n🔍 Now run: python scripts/advanced_figure_extractor.py")
        print("   to extract figures from these papers")

if __name__ == "__main__":
    main()