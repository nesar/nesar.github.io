#!/usr/bin/env python3
"""
Test script to specifically extract figures from Foundation Models papers
"""

import os
import subprocess
import tempfile
import shutil

def test_foundation_extraction():
    """Test extraction from a Foundation Models paper"""
    
    # Use a simple approach with existing tools
    print("🔬 Testing Foundation Models figure extraction...")
    
    # Try to download an AstroMLab paper from arXiv
    astromlab_url = "https://arxiv.org/pdf/2407.11194.pdf"  # AstroMLab 3 paper
    
    try:
        import requests
        
        # Download the paper
        print(f"📥 Downloading AstroMLab paper...")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(astromlab_url, headers=headers, stream=True, timeout=60)
        response.raise_for_status()
        
        # Save to temp file
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(temp_dir, "astromlab.pdf")
        
        with open(pdf_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Downloaded PDF ({os.path.getsize(pdf_path)} bytes)")
        
        # Use pdftoppm to convert to images
        print("🖼️  Converting PDF to images...")
        
        cmd = [
            'pdftoppm',
            '-png',
            '-r', '150',  # Lower resolution for testing
            pdf_path,
            os.path.join(temp_dir, 'page')
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            # List generated images
            page_files = [f for f in os.listdir(temp_dir) if f.startswith('page') and f.endswith('.png')]
            print(f"✅ Generated {len(page_files)} page images")
            
            # Copy a few sample pages to the research figures directory
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            figures_dir = os.path.join(base_dir, "images", "research", "figures")
            os.makedirs(figures_dir, exist_ok=True)
            
            # Copy first few pages as potential figures
            for i, page_file in enumerate(sorted(page_files)[:3]):  # First 3 pages
                src_path = os.path.join(temp_dir, page_file)
                dst_filename = f"astromlab_foundation_models_page{i+1}_manual.png"
                dst_path = os.path.join(figures_dir, dst_filename)
                
                shutil.copy2(src_path, dst_path)
                print(f"📋 Copied {dst_filename}")
            
            print("✅ Manual extraction completed!")
            print("💡 These are page images that may contain figures from the Foundation Models paper")
            
        else:
            print(f"❌ PDF conversion failed: {result.stderr}")
        
        # Cleanup
        shutil.rmtree(temp_dir)
        
    except ImportError:
        print("⚠️  requests module not available for download test")
    except Exception as e:
        print(f"❌ Error during test: {e}")

if __name__ == "__main__":
    test_foundation_extraction()