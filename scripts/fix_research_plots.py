#!/usr/bin/env python3
"""
Fix research plots by properly categorizing and selecting high-quality scientific figures
for each research area in the research page.
"""

import os
import re
import random
from pathlib import Path

class ResearchPlotFixer:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.figures_dir = self.base_dir / "images" / "research" / "figures"
        self.research_page = self.base_dir / "_pages" / "research.html"
        
        # Define research categories and their keywords for better categorization
        self.categories = {
            'foundation-models': {
                'keywords': ['astromlab', 'eaira', 'foundation', 'llm', 'language_model', 'ai_model'],
                'title': 'Foundation Models',
                'description': 'AstroMLab and EAIRA foundation models for astronomy'
            },
            'machine-learning': {
                'keywords': ['anomaly', 'generative', 'modular', 'deep_learning', 'neural', 'constructing'],
                'title': 'Machine Learning for Science', 
                'description': 'ML techniques for astronomical data analysis'
            },
            'dark-matter': {
                'keywords': ['caustic', 'dark_matter', 'cosmic_web', 'topology'],
                'title': 'Dark Matter & Cosmology',
                'description': 'Dark matter structure and cosmic web analysis'
            },
            'emulation-inference': {
                'keywords': ['probabilistic', 'reduced_order', 'emulation', 'surrogate', 'inference', 'application_of_probabilistic'],
                'title': 'Emulation & Inference',
                'description': 'Surrogate modeling and uncertainty quantification'
            }
        }
    
    def categorize_figures(self):
        """Categorize all figures in the figures directory."""
        categorized = {cat: [] for cat in self.categories.keys()}
        
        if not self.figures_dir.exists():
            print(f"❌ Figures directory not found: {self.figures_dir}")
            return categorized
        
        for fig_file in self.figures_dir.glob("*.png"):
            filename = fig_file.name.lower()
            
            # Skip JSON files and other non-images
            if not filename.endswith('.png'):
                continue
            
            # Categorize based on filename
            category_found = False
            for category, info in self.categories.items():
                for keyword in info['keywords']:
                    if keyword in filename:
                        categorized[category].append({
                            'filename': fig_file.name,
                            'path': f"/images/research/figures/{fig_file.name}",
                            'category': category
                        })
                        category_found = True
                        break
                if category_found:
                    break
        
        return categorized
    
    def select_best_figures(self, categorized_figs, max_per_category=4):
        """Select the best figures for each category."""
        selected = {}
        
        for category, figures in categorized_figs.items():
            if not figures:
                print(f"⚠️  No figures found for {category}")
                selected[category] = []
                continue
            
            # Prioritize certain figures
            priority_patterns = {
                'foundation-models': ['custom_logo', 'benchmark', 'methodology'],
                'machine-learning': ['anomaly_detection', 'generative', 'modular'],
                'dark-matter': ['caustic', 'topology'],
                'emulation-inference': ['probabilistic', 'application']
            }
            
            # Sort figures by priority and select diverse ones
            category_figs = figures.copy()
            random.shuffle(category_figs)  # Add randomization
            
            prioritized = []
            regular = []
            
            for fig in category_figs:
                is_priority = False
                for pattern in priority_patterns.get(category, []):
                    if pattern in fig['filename'].lower():
                        prioritized.append(fig)
                        is_priority = True
                        break
                if not is_priority:
                    regular.append(fig)
            
            # Select figures (prioritized first, then regular)
            selected_figs = prioritized[:max_per_category]
            remaining_slots = max_per_category - len(selected_figs)
            if remaining_slots > 0:
                selected_figs.extend(regular[:remaining_slots])
            
            selected[category] = selected_figs[:max_per_category]
            
            print(f"✅ Selected {len(selected[category])} figures for {category}")
            for fig in selected[category]:
                print(f"   - {fig['filename']}")
        
        return selected
    
    def update_research_page(self, selected_figures):
        """Update the research page with selected figures."""
        if not self.research_page.exists():
            print(f"❌ Research page not found: {self.research_page}")
            return False
        
        with open(self.research_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update each section
        section_mappings = {
            'foundation-models': 'Foundation Models',
            'machine-learning': 'Machine Learning for Science', 
            'dark-matter': 'Dark Matter & Cosmology',
            'emulation-inference': 'Emulation & Inference'
        }
        
        for category, section_title in section_mappings.items():
            figures = selected_figures.get(category, [])
            
            # Create HTML for figures
            if figures:
                figures_html = ""
                for fig in figures:
                    figures_html += f'''        <div class="preview-figure">
          <img src="{fig['path']}" alt="Research preview" onclick="openModal(this)" />
        </div>

'''
                figures_html = figures_html.rstrip() + "\n"
            else:
                figures_html = '''        <div class="no-figures">
          <p>Representative figures coming soon...</p>
        </div>

'''
            
            # Find and replace the figures section for this category
            # Look for the section by finding the title and then the figures div
            pattern = rf'(<a href="[^"]*" class="research-title">{re.escape(section_title)}</a>.*?<div class="research-preview-figures">\s*)(.*?)(\s*</div>\s*</div>)'
            
            def replace_figures(match):
                before = match.group(1)
                after = match.group(3)
                return f"{before}\n{figures_html}{after}"
            
            content = re.sub(pattern, replace_figures, content, flags=re.DOTALL)
        
        # Write updated content
        with open(self.research_page, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated research page: {self.research_page}")
        return True

def main():
    print("🔧 Fixing research plots...")
    
    fixer = ResearchPlotFixer()
    
    # Categorize existing figures
    print("\n📂 Categorizing figures...")
    categorized = fixer.categorize_figures()
    
    # Print summary
    total_figures = sum(len(figs) for figs in categorized.values())
    print(f"\n📊 Found {total_figures} total figures:")
    for category, figures in categorized.items():
        print(f"   {category}: {len(figures)} figures")
    
    # Select best figures for each category
    print("\n🎯 Selecting best figures...")
    selected = fixer.select_best_figures(categorized, max_per_category=4)
    
    # Update research page
    print("\n📝 Updating research page...")
    success = fixer.update_research_page(selected)
    
    if success:
        print("\n🎉 Research plots fixed successfully!")
        print("\n📋 Summary:")
        for category, figures in selected.items():
            cat_info = fixer.categories[category]
            print(f"   {cat_info['title']}: {len(figures)} high-quality scientific figures")
    else:
        print("\n❌ Failed to update research page")

if __name__ == "__main__":
    main()