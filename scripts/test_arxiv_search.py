#!/usr/bin/env python3
"""
Test script to debug arXiv search for Azton Wells
"""
import requests
import xml.etree.ElementTree as ET
import re
from urllib.parse import quote

def test_arxiv_search():
    search_terms = [
        "au:\"Azton Wells\"",
        "au:\"Wells, Azton\"", 
        "au:\"Azton I Wells\"",
        "au:\"Wells, Azton I\"",
        "au:\"A I Wells\"",
        "au:Wells AND au:Azton"
    ]
    
    author_patterns = [
        r"(Wells.*Azton)",
        r"(Wells.*A[\s\.])",
        r"(A\.?\s*I?\.?\s*Wells)"
    ]
    
    all_papers = []
    
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
            
            for j, entry in enumerate(entries):
                # Extract basic info
                title = entry.find('./atom:title', namespace)
                authors = []
                for author in entry.findall('./atom:author', namespace):
                    name_elem = author.find('./atom:name', namespace)
                    if name_elem is not None:
                        authors.append(name_elem.text.strip())
                
                if title is not None and authors:
                    print(f"  {j+1}. {title.text.strip()[:60]}...")
                    print(f"     Authors: {authors}")
                    
                    # Test author matching
                    is_author = False
                    for pattern in author_patterns:
                        for author in authors:
                            if re.search(pattern, author, re.IGNORECASE):
                                is_author = True
                                print(f"     ✅ MATCH with pattern: {pattern}")
                                break
                        if is_author:
                            break
                    
                    if not is_author:
                        print(f"     ❌ No match with patterns")
                    
                    print()
            
            if len(entries) == 0:
                print("❌ No entries found for this search term")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_arxiv_search()