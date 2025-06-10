#!/usr/bin/env python3
"""
Simple validation script to check the Jekyll site structure and content.
"""

import os
import re
import yaml

def validate_yaml_frontmatter(filepath):
    """Validate YAML front matter in a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for YAML front matter
        yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not yaml_match:
            return False, "No YAML front matter found"
        
        yaml_content = yaml_match.group(1)
        
        # Try to parse YAML (basic validation)
        try:
            parsed = yaml.safe_load(yaml_content)
            if not isinstance(parsed, dict):
                return False, "YAML front matter is not a valid dict"
        except yaml.YAMLError as e:
            return False, f"YAML parsing error: {e}"
        
        return True, "Valid"
    
    except Exception as e:
        return False, f"File reading error: {e}"

def validate_directory(directory, file_extension=".md"):
    """Validate all files in a directory."""
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist")
        return
    
    print(f"\nValidating {directory}:")
    print("-" * 40)
    
    files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
    valid_count = 0
    
    for filename in sorted(files):
        filepath = os.path.join(directory, filename)
        is_valid, message = validate_yaml_frontmatter(filepath)
        
        status = "✓" if is_valid else "✗"
        print(f"{status} {filename}: {message}")
        
        if is_valid:
            valid_count += 1
    
    print(f"\nSummary: {valid_count}/{len(files)} files are valid")

def check_navigation():
    """Check navigation structure."""
    nav_file = "_data/navigation.yml"
    
    if not os.path.exists(nav_file):
        print("Navigation file not found")
        return
    
    print("\nNavigation structure:")
    print("-" * 40)
    
    try:
        with open(nav_file, 'r') as f:
            nav_data = yaml.safe_load(f)
        
        if 'main' in nav_data:
            for item in nav_data['main']:
                title = item.get('title', 'No title')
                url = item.get('url', 'No URL')
                print(f"• {title} -> {url}")
    
    except Exception as e:
        print(f"Error reading navigation: {e}")

def check_config():
    """Check Jekyll configuration."""
    config_file = "_config.yml"
    
    if not os.path.exists(config_file):
        print("Jekyll config file not found")
        return
    
    print("\nJekyll configuration:")
    print("-" * 40)
    
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        important_keys = ['title', 'description', 'url', 'baseurl', 'author']
        for key in important_keys:
            value = config.get(key, 'Not set')
            print(f"• {key}: {value}")
    
    except Exception as e:
        print(f"Error reading config: {e}")

def main():
    print("Jekyll Site Validation Report")
    print("=" * 50)
    
    # Check configuration
    check_config()
    
    # Check navigation
    check_navigation()
    
    # Validate different collections
    validate_directory("_publications")
    validate_directory("_portfolio")
    validate_directory("_pages")
    
    # Check for required assets
    print("\nAsset files:")
    print("-" * 40)
    
    asset_files = [
        "assets/css/main.scss",
        "assets/css/custom.css",
        "_includes/head/custom.html"
    ]
    
    for asset in asset_files:
        exists = "✓" if os.path.exists(asset) else "✗"
        print(f"{exists} {asset}")
    
    print("\nValidation complete!")

if __name__ == "__main__":
    main()