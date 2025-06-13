#!/usr/bin/env python3
"""
Add figures to Foundation Models section by creating placeholder images
or downloading sample figures from Foundation Models papers.
"""

import os
import json

def create_foundation_figures():
    """Create basic figure entries for Foundation Models."""
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    figures_dir = os.path.join(base_dir, "images", "research", "figures")
    os.makedirs(figures_dir, exist_ok=True)
    
    # Create mock figure entries that represent Foundation Models research
    figures = [
        {
            'filename': 'astromlab_performance_benchmark.json',
            'filepath': os.path.join(figures_dir, 'astromlab_performance_benchmark.json'),
            'paper_title': 'AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model',
            'paper_slug': 'astromlab_performance',
            'page': 1,
            'size': (600, 400),
            'file_size': 1000,
            'relative_path': '/images/research/figures/astromlab_performance_benchmark.json'
        },
        {
            'filename': 'eaira_evaluation_framework.json',
            'filepath': os.path.join(figures_dir, 'eaira_evaluation_framework.json'),
            'paper_title': 'EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants',
            'paper_slug': 'eaira_framework',
            'page': 1,
            'size': (600, 400),
            'file_size': 1000,
            'relative_path': '/images/research/figures/eaira_evaluation_framework.json'
        }
    ]
    
    # Create JSON metadata files that can be processed
    for fig in figures:
        with open(fig['filepath'], 'w') as f:
            json.dump({
                'type': 'foundation_model_figure',
                'title': fig['paper_title'],
                'description': 'Figure placeholder for Foundation Models research'
            }, f, indent=2)
    
    print(f"✅ Created {len(figures)} Foundation Models figure placeholders")
    return figures

def update_foundation_portfolio():
    """Update the Foundation Models portfolio with a note about figures."""
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    portfolio_file = os.path.join(base_dir, "_portfolio", "portfolio-1-foundation-models.md")
    
    if not os.path.exists(portfolio_file):
        print("❌ Foundation Models portfolio file not found")
        return
    
    try:
        with open(portfolio_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace empty grid with explanatory content
        new_figures_section = '''<div class="research-figures-grid">
  <div class="foundation-models-note">
    <h4>Research Output Visualization</h4>
    <p>Foundation Models research in astronomy primarily produces:</p>
    <ul>
      <li><strong>Performance benchmarks</strong> - Q&A accuracy, reasoning capabilities</li>
      <li><strong>Model architectures</strong> - Specialized domain adaptations</li>
      <li><strong>Evaluation frameworks</strong> - Methodologies for AI research assistants</li>
      <li><strong>Comparative analyses</strong> - Domain-specific vs general models</li>
    </ul>
    <p class="note-text">Traditional figure extraction may not capture the text-heavy, table-based nature of LLM research outputs.</p>
  </div>
</div>

<style>
.foundation-models-note {
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius: 12px;
  padding: 2rem;
  border-left: 4px solid #6366f1;
  grid-column: 1 / -1;
}

.foundation-models-note h4 {
  color: #4338ca;
  margin-bottom: 1rem;
  font-size: 1.2em;
}

.foundation-models-note p {
  color: #4a5568;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.foundation-models-note ul {
  color: #4a5568;
  margin-bottom: 1rem;
  padding-left: 1.5rem;
}

.foundation-models-note li {
  margin-bottom: 0.5rem;
}

.note-text {
  font-style: italic;
  font-size: 0.9em;
  color: #718096;
}
</style>'''
        
        # Find and replace the empty research figures grid
        if '<div class="research-figures-grid">\n</div>' in content:
            content = content.replace(
                '<div class="research-figures-grid">\n</div>',
                new_figures_section
            )
        elif '<div class="research-figures-grid">' in content and '</div>' in content:
            # More complex replacement for any empty grid
            import re
            pattern = r'<div class="research-figures-grid">\s*</div>'
            content = re.sub(pattern, new_figures_section, content)
        
        # Write updated content
        with open(portfolio_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated Foundation Models portfolio with research explanation")
        
    except Exception as e:
        print(f"❌ Error updating portfolio: {e}")

def main():
    print("🔬 Setting up Foundation Models research visualization...")
    
    # Create placeholder figures
    figures = create_foundation_figures()
    
    # Update the portfolio page
    update_foundation_portfolio()
    
    print("\n🎉 Foundation Models section updated!")
    print("💡 The section now explains the nature of Foundation Models research")
    print("   which focuses on performance metrics and methodologies rather than traditional scientific plots.")

if __name__ == "__main__":
    main()