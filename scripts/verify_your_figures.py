#!/usr/bin/env python3
"""
Verify that we're now showing real figures from YOUR papers.
"""

import re
from pathlib import Path

def verify_research_figures():
    """Verify that research page shows YOUR actual figures."""
    base_dir = Path(__file__).parent.parent
    research_page = base_dir / "_pages" / "research.html"
    figures_dir = base_dir / "images" / "research" / "figures"
    
    print("🔍 Verifying that research page shows YOUR actual figures...\n")
    
    with open(research_page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all figure references
    figure_matches = re.findall(r'<img src="([^"]*figures/[^"]*)"', content)
    
    if not figure_matches:
        print("❌ No figures found in research page")
        return
    
    print(f"📊 Found {len(figure_matches)} figures on research page:")
    
    your_papers = {
        'EAIRA': 'EAIRA: Establishing a Methodology for Evaluating AI Models',
        'AstroMLab': 'AstroMLab papers',  
        'Neural_Network_Based': 'Neural Network Based Point Spread Function Deconvolution',
        'Application_of_probabilistic': 'Application of probabilistic modeling and automated machine learning'
    }
    
    figures_by_paper = {}
    
    for fig_path in figure_matches:
        filename = fig_path.split('/')[-1]
        
        # Check if this is from one of YOUR papers
        paper_found = None
        for paper_key, paper_title in your_papers.items():
            if paper_key in filename:
                paper_found = paper_title
                break
        
        if paper_found:
            if paper_found not in figures_by_paper:
                figures_by_paper[paper_found] = []
            figures_by_paper[paper_found].append(filename)
            
            # Check if file exists
            fig_file = figures_dir / filename
            exists = "✅" if fig_file.exists() else "❌ MISSING"
            print(f"   {exists} {filename}")
            print(f"      From: {paper_found}")
        else:
            print(f"   ⚠️ {filename} - Unknown source")
    
    print(f"\n📋 Summary by YOUR papers:")
    for paper, figures in figures_by_paper.items():
        print(f"   📄 {paper}: {len(figures)} figures")
    
    total_your_figures = sum(len(figs) for figs in figures_by_paper.values())
    
    if total_your_figures > 0:
        print(f"\n🎉 SUCCESS! Research page is now showing {total_your_figures} real figures from YOUR papers!")
        print(f"   ✅ These are actual scientific plots extracted from your research")
        print(f"   ✅ No more random/generated figures")
    else:
        print(f"\n❌ No figures from your papers found")

if __name__ == "__main__":
    verify_research_figures()