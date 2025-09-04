#!/usr/bin/env python3
"""
Debug script to check arXiv search for Nesar Ramachandra
"""
import requests
import xml.etree.ElementTree as ET
import re
from urllib.parse import quote

def debug_nesar_search():
    search_terms = [
        "au:\"Nesar S Ramachandra\"",
        "au:\"Ramachandra, Nesar\"", 
        "au:\"N S Ramachandra\"",
        "au:Ramachandra AND au:Nesar",
        "au:\"Ramachandra, N S\"",
        "au:\"Ramachandra, N.S.\"",
        "au:\"N.S. Ramachandra\"",
        "au:\"Nesar Ramachandra\""
    ]
    
    author_patterns = [
        r"(Ramachandra.*Nesar)",
        r"(Ramachandra.*N[\s\.])",
        r"(N\.?\s*S?\.?\s*Ramachandra)"
    ]
    
    all_papers = []
    seen_arxiv_ids = set()
    
    for i, search_term in enumerate(search_terms):
        print(f"\n--- Testing search term {i+1}: {search_term} ---")
        
        encoded_search = quote(search_term)
        url = f"http://export.arxiv.org/api/query?search_query={encoded_search}&sortBy=submittedDate&sortOrder=descending&max_results=50"
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            print(f"✅ HTTP {response.status_code}")
            
            root = ET.fromstring(response.content)
            namespace = {'atom': 'http://www.w3.org/2005/Atom'}
            
            entries = root.findall('.//atom:entry', namespace)
            print(f"Found {len(entries)} total entries")
            
            papers_found_this_search = 0
            for j, entry in enumerate(entries):
                # Extract basic info
                title = entry.find('./atom:title', namespace)
                arxiv_id = entry.find('./atom:id', namespace)
                authors = []
                for author in entry.findall('./atom:author', namespace):
                    name_elem = author.find('./atom:name', namespace)
                    if name_elem is not None:
                        authors.append(name_elem.text.strip())
                
                if title is not None and authors and arxiv_id is not None:
                    # Extract arXiv ID for deduplication
                    arxiv_url = arxiv_id.text
                    arxiv_match = re.search(r'(\d+\.\d+)', arxiv_url)
                    arxiv_number = arxiv_match.group(1) if arxiv_match else ""
                    
                    # Skip if already seen
                    if arxiv_number in seen_arxiv_ids:
                        continue
                    
                    print(f"  Entry {j+1}:")
                    print(f"    Title: {title.text.strip()[:70]}...")
                    print(f"    Authors: {authors}")
                    print(f"    ArXiv ID: {arxiv_number}")
                    
                    # Test author matching with patterns
                    is_author = False
                    matching_pattern = None
                    
                    for pattern in author_patterns:
                        for author in authors:
                            if re.search(pattern, author, re.IGNORECASE):
                                is_author = True
                                matching_pattern = pattern
                                print(f"    ✅ MATCH with pattern: '{pattern}' on author: '{author}'")
                                break
                        if is_author:
                            break
                    
                    if not is_author:
                        print(f"    ❌ No match with any pattern")
                        # Test if any author contains both key parts
                        for author in authors:
                            if 'ramachandra' in author.lower() and 'nesar' in author.lower():
                                print(f"    🟡 Would match with simple check: '{author}'")
                    else:
                        seen_arxiv_ids.add(arxiv_number)
                        papers_found_this_search += 1
                        all_papers.append({
                            'title': title.text.strip(),
                            'authors': authors,
                            'arxiv_id': arxiv_number,
                            'search_term': search_term,
                            'matching_pattern': matching_pattern
                        })
                    
                    print()
            
            print(f"Papers matched for this search: {papers_found_this_search}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print(f"\n=== FINAL RESULTS ===")
    print(f"Total unique papers found: {len(all_papers)}")
    for i, paper in enumerate(all_papers):
        print(f"{i+1}. {paper['title'][:60]}...")
        print(f"   Search term: {paper['search_term']}")
        print(f"   Pattern: {paper['matching_pattern']}")
        print(f"   ArXiv: {paper['arxiv_id']}")
        print()

if __name__ == "__main__":
    debug_nesar_search()