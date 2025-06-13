#!/usr/bin/env python3
"""
Download more papers for Dark Matter and Emulation categories.
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
    """Download more papers for missing categories."""
    
    # Papers for missing categories
    papers = [
        # Dark Matter & Cosmology papers
        {
            'url': 'https://arxiv.org/pdf/1704.04221.pdf',  # Topology and geometry of dark matter web
            'filename': 'topology_geometry_dark_matter_web.pdf'
        },
        {
            'url': 'https://arxiv.org/pdf/1810.07703.pdf',  # Caustic design of dark matter web
            'filename': 'caustic_design_dark_matter_web.pdf'
        },
        # Emulation & Inference papers  
        {
            'url': 'https://arxiv.org/pdf/2005.00677.pdf',  # Probabilistic neural networks
            'filename': 'probabilistic_neural_networks.pdf'
        }
    ]
    
    print(f"🚀 Downloading {len(papers)} additional papers...")
    
    downloaded = []
    for paper in papers:
        filepath = download_paper(paper['url'], paper['filename'])
        if filepath:
            downloaded.append(filepath)
        time.sleep(2)  # Be nice to servers
    
    print(f"\n📊 Downloaded {len(downloaded)} papers successfully")
    
    if downloaded:
        print("\n🔍 Now run: python scripts/advanced_figure_extractor.py")
        print("   to extract figures from these additional papers")

if __name__ == "__main__":
    main()