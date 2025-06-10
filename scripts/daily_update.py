#!/usr/bin/env python3
"""
Daily automation script for updating Nesar's academic website.
Run this script regularly to keep the website up to date.
"""

import os
import sys
import subprocess
from datetime import datetime

def run_command(cmd, description):
    """Run a command and print status."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"❌ {description} failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} failed with exception: {e}")
        return False

def main():
    print("🚀 Starting daily website update")
    print("=" * 50)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Change to website directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    website_dir = os.path.dirname(script_dir)
    os.chdir(website_dir)
    
    print(f"📁 Working directory: {website_dir}")
    print()
    
    success_count = 0
    total_tasks = 5
    
    # Task 1: Clean publications
    if run_command("python scripts/automated_update.py clean", "Cleaning duplicate publications"):
        success_count += 1
    
    # Task 2: Update research portfolio
    if run_command("python scripts/automated_update.py update-research", "Updating research portfolio"):
        success_count += 1
    
    # Task 3: Extract figures from papers
    if run_command("python scripts/automated_update.py extract-figures", "Extracting figures from papers"):
        success_count += 1
    
    # Task 4: Validate site structure
    if run_command("python scripts/validate_site.py", "Validating site structure"):
        success_count += 1
    
    # Task 5: List current publications for review
    if run_command("python scripts/automated_update.py list > publication_list.txt", "Generating publication list"):
        success_count += 1
        print("📄 Publication list saved to publication_list.txt")
    
    print()
    print("📊 Summary")
    print("-" * 20)
    print(f"✅ {success_count}/{total_tasks} tasks completed successfully")
    
    if success_count == total_tasks:
        print("🎉 All tasks completed successfully!")
        print()
        print("💡 Next steps:")
        print("   1. Review publication_list.txt for any issues")
        print("   2. Test locally with: bundle exec jekyll serve")
        print("   3. Commit and push changes to deploy")
        return 0
    else:
        print("⚠️  Some tasks failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())