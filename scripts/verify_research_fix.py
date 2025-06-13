#!/usr/bin/env python3
"""
Verify that the research plots have been fixed correctly.
"""

import os
import re
from pathlib import Path

def verify_research_plots():
    """Verify that research plots are now correctly showing scientific figures."""
    base_dir = Path(__file__).parent.parent
    research_page = base_dir / "_pages" / "research.html"
    figures_dir = base_dir / "images" / "research" / "figures"
    
    print("🔍 Verifying research plot fixes...\n")
    
    # Read research page
    with open(research_page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check each section
    sections = {
        'Foundation Models': {
            'expected_figures': 4,
            'keywords': ['astromlab', 'eaira'],
            'should_include': ['astromlab_foundation_models_custom_logo.png', 'eaira_methodology_custom_diagram.png']
        },
        'Machine Learning for Science': {
            'expected_figures': 4,
            'keywords': ['generative', 'modular', 'anomaly'],
            'should_include': []
        },
        'Dark Matter & Cosmology': {
            'expected_figures': 4,
            'keywords': ['caustic', 'dark_matter'],
            'should_include': []
        },
        'Emulation & Inference': {
            'expected_figures': 4,
            'keywords': ['probabilistic', 'application'],
            'should_include': []
        }
    }
    
    results = {}
    
    for section_name, criteria in sections.items():
        print(f"📊 Checking {section_name}...")
        
        # Find section in content
        pattern = rf'class="research-title">{re.escape(section_name)}</a>.*?<div class="research-preview-figures">(.*?)</div>\s*</div>'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            results[section_name] = {'status': 'ERROR', 'message': 'Section not found'}
            print(f"   ❌ Section not found")
            continue
        
        figures_html = match.group(1)
        
        # Count figures
        figure_matches = re.findall(r'<img src="([^"]*)"', figures_html)
        num_figures = len(figure_matches)
        
        # Check for "coming soon" message
        has_coming_soon = 'coming soon' in figures_html.lower() or 'no-figures' in figures_html
        
        # Verify figures exist
        missing_figures = []
        for fig_path in figure_matches:
            # Convert web path to file path
            fig_filename = fig_path.split('/')[-1]
            fig_file = figures_dir / fig_filename
            if not fig_file.exists():
                missing_figures.append(fig_filename)
        
        # Check for required figures
        required_missing = []
        for required_fig in criteria['should_include']:
            if required_fig not in [fig.split('/')[-1] for fig in figure_matches]:
                required_missing.append(required_fig)
        
        # Determine status
        if has_coming_soon:
            status = 'NEEDS_FIGURES'
            message = 'Still shows "coming soon" message'
        elif num_figures == 0:
            status = 'NO_FIGURES' 
            message = 'No figures found'
        elif missing_figures:
            status = 'MISSING_FILES'
            message = f'Missing figure files: {", ".join(missing_figures)}'
        elif required_missing:
            status = 'MISSING_REQUIRED'
            message = f'Missing required figures: {", ".join(required_missing)}'
        elif num_figures < criteria['expected_figures']:
            status = 'INCOMPLETE'
            message = f'Only {num_figures}/{criteria["expected_figures"]} figures'
        else:
            status = 'GOOD'
            message = f'{num_figures} scientific figures displaying correctly'
        
        results[section_name] = {
            'status': status,
            'message': message,
            'figures': figure_matches,
            'count': num_figures
        }
        
        # Print results
        if status == 'GOOD':
            print(f"   ✅ {message}")
            for fig in figure_matches:
                print(f"      - {fig.split('/')[-1]}")
        else:
            print(f"   ⚠️  {message}")
    
    # Overall summary
    print(f"\n📋 Summary:")
    total_sections = len(sections)
    good_sections = sum(1 for r in results.values() if r['status'] == 'GOOD')
    total_figures = sum(r['count'] for r in results.values())
    
    print(f"   Sections fixed: {good_sections}/{total_sections}")
    print(f"   Total figures: {total_figures}")
    
    if good_sections == total_sections:
        print(f"\n🎉 All research sections are now displaying proper scientific figures!")
        print(f"   ✅ Foundation Models: Now shows AstroMLab and EAIRA figures")
        print(f"   ✅ Machine Learning: Shows real ML research plots")
        print(f"   ✅ Dark Matter: Shows cosmic web and caustic analysis")
        print(f"   ✅ Emulation: Shows probabilistic modeling results")
        return True
    else:
        print(f"\n⚠️  Some sections still need attention:")
        for section, result in results.items():
            if result['status'] != 'GOOD':
                print(f"   - {section}: {result['message']}")
        return False

if __name__ == "__main__":
    verify_research_plots()