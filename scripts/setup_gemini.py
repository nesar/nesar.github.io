#!/usr/bin/env python3
"""
Setup script for Gemini API integration.
This helps configure the Gemini API key for LLM-generated summaries.
"""

import os
from pathlib import Path

def setup_gemini_api():
    """Setup Gemini API key for research overhaul."""
    
    print("🤖 Gemini API Setup for Research Overhaul")
    print("=" * 50)
    print()
    print("To use LLM-generated research summaries, you need a Gemini API key.")
    print("If you don't have one or prefer not to use LLM, the script will use fallback summaries.")
    print()
    
    choice = input("Do you want to set up Gemini API? (y/n): ").lower().strip()
    
    if choice != 'y':
        print("✅ Skipping Gemini setup. The script will use fallback summaries.")
        return
    
    print()
    print("📋 Steps to get Gemini API key:")
    print("1. Go to: https://makersuite.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Create API Key'")
    print("4. Copy the generated API key")
    print()
    
    api_key = input("Enter your Gemini API key (or press Enter to skip): ").strip()
    
    if not api_key:
        print("✅ Skipping API key setup. The script will use fallback summaries.")
        return
    
    # Set environment variable for current session
    os.environ['GEMINI_API_KEY'] = api_key
    
    # Try to add to shell profile for persistence
    home = Path.home()
    shell_profiles = [
        home / ".bashrc",
        home / ".zshrc", 
        home / ".bash_profile",
        home / ".profile"
    ]
    
    for profile in shell_profiles:
        if profile.exists():
            try:
                with open(profile, 'r') as f:
                    content = f.read()
                
                if 'GEMINI_API_KEY' not in content:
                    with open(profile, 'a') as f:
                        f.write(f"\n# Gemini API Key for research overhaul\nexport GEMINI_API_KEY='{api_key}'\n")
                    print(f"✅ Added API key to {profile}")
                    break
                else:
                    print(f"✅ API key already in {profile}")
                    break
            except Exception as e:
                continue
    
    print("✅ Gemini API key configured!")
    print("💡 You may need to restart your terminal or run: source ~/.bashrc")
    print()
    print("🚀 Now you can run: python scripts/research_overhaul.py")

if __name__ == "__main__":
    setup_gemini_api()