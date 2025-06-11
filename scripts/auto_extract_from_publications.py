#!/usr/bin/env python3
"""
Automatically extract figures from existing publications in the _publications directory.
"""

import os
import re
import sys
from extract_figures import FigureExtractor

def get_publications_with_urls():
    """Get all publications with PDF URLs."""
    pub_dir = "_publications"
    publications = []
    
    for filename in os.listdir(pub_dir):
        if not filename.endswith('.md'):
            continue
        
        try:
            with open(os.path.join(pub_dir, filename), 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract metadata
            title_match = re.search(r'title:\s*["\'](.*?)["\']', content, re.DOTALL)
            paperurl_match = re.search(r'paperurl:\s*["\']([^"\']+)["\']', content)
            excerpt_match = re.search(r'excerpt:\s*["\'].*?\[(.*?)\]\(([^)]+)\).*?["\']', content)
            
            title = title_match.group(1) if title_match else "Unknown"
            
            # Get URL from paperurl or excerpt
            url = ""
            if paperurl_match:
                url = paperurl_match.group(1)
            elif excerpt_match:
                url = excerpt_match.group(2)
            
            # Only process papers with arXiv or direct PDF URLs
            if url and ('arxiv.org' in url or url.endswith('.pdf') or 'doi.org' in url):
                publications.append({
                    'title': title,
                    'url': url,
                    'filename': filename
                })
                
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    
    return publications

def main():
    extractor = FigureExtractor()
    publications = get_publications_with_urls()
    
    print(f"Found {len(publications)} publications with URLs")
    print("Note: Figure selection is randomized for variety across different runs.")
    
    # Process papers from different categories with better Foundation Models coverage
    key_papers = [
        "AstroMLab",
        "EAIRA", 
        "foundation model",
        "language model",
        "machine learning",
        "dark matter",
        "neural network",
        "uncertainty quantification",
        "bayesian",
        "probabilistic",
        "gravitational lens",
        "lensing",
        "anomaly detection",
        "generative",
        "deconvolution",
        "emulator",
        "surrogate",
        "cosmic web",
        "caustic",
        "multistream"
    ]
    
    processed_count = 0
    max_papers = 12  # Increased limit to get more figures
    
    # Randomize the order of publications for variety
    import random
    random.shuffle(publications)
    
    for pub in publications:
        if processed_count >= max_papers:
            break
            
        title = pub['title']
        url = pub['url']
        
        # Check if it's a key paper with more comprehensive matching
        is_key_paper = any(keyword.lower() in title.lower() for keyword in key_papers)
        
        # Special handling for Foundation Models papers that might not have extractable figures
        is_foundation_model = any(keyword in title.lower() for keyword in ['astromlab', 'eaira', 'llm', 'language model', 'foundation model'])
        
        if not is_key_paper:
            continue
            
        print(f"\nProcessing: {title}")
        print(f"URL: {url}")
        
        # Try to extract figures
        try:
            # Download PDF
            pdf_path = extractor.download_pdf_from_url(url, title)
            
            if pdf_path and os.path.exists(pdf_path):
                # Extract figures
                figures = extractor.extract_from_pdf(pdf_path, title)
                
                if figures:
                    # Categorize and update portfolio
                    paper_info = extractor.get_paper_info_from_title(title)
                    figures_by_category = {}
                    
                    for fig in figures:
                        category = extractor.categorize_figure(fig, paper_info)
                        if category not in figures_by_category:
                            figures_by_category[category] = []
                        figures_by_category[category].append(fig)
                    
                    # Update research portfolio
                    extractor.update_research_with_figures(figures_by_category)
                    
                    print(f"✅ Extracted {len(figures)} figures:")
                    for cat, figs in figures_by_category.items():
                        print(f"   {cat}: {len(figs)} figures")
                    
                    processed_count += 1
                else:
                    print("⚠️  No figures extracted")
                    # For Foundation Models papers, this is expected as they may not have traditional scientific figures
                    if is_foundation_model:
                        print("   (This is normal for Foundation Models papers - they typically contain text/performance tables rather than extractable figures)")
                
                # Clean up
                try:
                    os.remove(pdf_path)
                except:
                    pass
            else:
                print("❌ Failed to download PDF")
                
        except Exception as e:
            print(f"❌ Error processing {title}: {e}")
    
    print(f"\n🎉 Processed {processed_count} papers successfully!")
    
    if processed_count > 0:
        print("\n💡 Next steps:")
        print("1. Check the updated research portfolio pages")
        print("2. Review extracted figures in images/research/figures/")
        print("3. Test the website locally to see the results")
        print("4. Run this script again for different figure selections (randomized)")
    
    # Print summary of categories that might need attention
    print("\n📝 Note about Foundation Models:")
    print("   Foundation Models papers (AstroMLab, EAIRA) typically don't contain")
    print("   extractable scientific figures but rather text, tables, and performance metrics.")
    print("   Consider adding custom figures or logos for this research area.")

if __name__ == "__main__":
    main()