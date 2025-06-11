#!/usr/bin/env python3
"""
Create custom figures for Foundation Models research area.
Since LLM papers typically don't have extractable scientific figures,
this script creates placeholder or logo-style figures for the Foundation Models section.
"""

import os
import requests
from PIL import Image, ImageDraw, ImageFont
import io
import textwrap

class FoundationModelsFigureCreator:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.figures_dir = os.path.join(self.base_dir, "images", "research", "figures")
        os.makedirs(self.figures_dir, exist_ok=True)
        
    def create_astromlab_logo_figure(self):
        """Create a figure representing AstroMLab research."""
        width, height = 800, 600
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        
        # Try to load a font, fallback to default if not available
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 60)
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 30)
            text_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 20)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
        
        # Background gradient effect (simplified)
        for y in range(height):
            shade = int(255 - (y / height) * 40)
            color = (shade, shade, 255)
            draw.line([(0, y), (width, y)], fill=color)
        
        # Title
        title = "AstroMLab"
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (width - title_width) // 2
        draw.text((title_x, 100), title, fill='white', font=title_font)
        
        # Subtitle
        subtitle = "Foundation Models for Astronomy"
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        subtitle_x = (width - subtitle_width) // 2
        draw.text((subtitle_x, 180), subtitle, fill='white', font=subtitle_font)
        
        # Key achievements
        achievements = [
            "• Specialized 8B & 70B parameter models",
            "• GPT-4o level performance in astronomy",
            "• Benchmark-topping Q&A capabilities",
            "• Domain-specific reasoning architecture"
        ]
        
        y_start = 280
        for i, achievement in enumerate(achievements):
            draw.text((100, y_start + i * 40), achievement, fill='navy', font=text_font)
        
        # Save the figure
        filename = "astromlab_foundation_models_custom_logo.png"
        filepath = os.path.join(self.figures_dir, filename)
        img.save(filepath, "PNG")
        
        return {
            'filename': filename,
            'filepath': filepath,
            'paper_title': 'AstroMLab: Foundation Models for Astronomy',
            'paper_slug': 'astromlab_foundation_models',
            'page': 1,
            'size': (width, height),
            'file_size': os.path.getsize(filepath),
            'relative_path': f"/images/research/figures/{filename}"
        }
    
    def create_eaira_methodology_figure(self):
        """Create a figure representing EAIRA methodology."""
        width, height = 800, 600
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        
        # Try to load a font, fallback to default if not available
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 50)
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 25)
            text_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 18)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
        
        # Background gradient effect (green theme)
        for y in range(height):
            shade = int(255 - (y / height) * 60)
            color = (220, shade, 220)
            draw.line([(0, y), (width, y)], fill=color)
        
        # Title
        title = "EAIRA"
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (width - title_width) // 2
        draw.text((title_x, 80), title, fill='darkgreen', font=title_font)
        
        # Subtitle
        subtitle = "Evaluating AI Models as Research Assistants"
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        subtitle_x = (width - subtitle_width) // 2
        draw.text((subtitle_x, 150), subtitle, fill='darkgreen', font=subtitle_font)
        
        # Methodology components
        components = [
            "📊 Comprehensive Evaluation Framework",
            "🔬 Scientific Research Task Assessment", 
            "🤖 AI Model Performance Benchmarking",
            "📈 Methodology for Research Assistant Evaluation"
        ]
        
        y_start = 240
        for i, component in enumerate(components):
            draw.text((80, y_start + i * 50), component, fill='darkblue', font=text_font)
        
        # Draw some simple geometric elements
        draw.rectangle([50, 480, 750, 550], outline='darkgreen', width=3)
        draw.text((60, 495), "Establishing Standards for AI Research Assistants", fill='darkgreen', font=text_font)
        
        # Save the figure
        filename = "eaira_methodology_custom_diagram.png"
        filepath = os.path.join(self.figures_dir, filename)
        img.save(filepath, "PNG")
        
        return {
            'filename': filename,
            'filepath': filepath,
            'paper_title': 'EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants',
            'paper_slug': 'eaira_methodology',
            'page': 1,
            'size': (width, height),
            'file_size': os.path.getsize(filepath),
            'relative_path': f"/images/research/figures/{filename}"
        }
    
    def update_foundation_models_portfolio(self, figures):
        """Update the Foundation Models portfolio with custom figures."""
        portfolio_file = os.path.join(self.base_dir, "_portfolio", "portfolio-1-foundation-models.md")
        
        if not os.path.exists(portfolio_file):
            print(f"Portfolio file not found: {portfolio_file}")
            return
        
        try:
            with open(portfolio_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Create figures HTML
            figures_html = '<div class="research-figures-grid">\n'
            
            for fig in figures:
                figures_html += f'''  <div class="research-figure">
    <img src="{fig['relative_path']}" alt="Figure from {fig['paper_title']}" onclick="openModal(this)">
    <p class="figure-caption">From: {fig['paper_title'][:80]}{'...' if len(fig['paper_title']) > 80 else ''}</p>
  </div>
'''
            
            figures_html += '</div>\n'
            
            # Find and replace the research figures section
            if "## Research Figures" in content:
                # Find the start and end of the figures section
                start_marker = "## Research Figures"
                end_marker = "## Related Publications"
                
                start_idx = content.find(start_marker)
                end_idx = content.find(end_marker)
                
                if start_idx != -1 and end_idx != -1:
                    # Replace the content between markers
                    before = content[:start_idx]
                    after = content[end_idx:]
                    
                    new_content = before + f"{start_marker}\n\n{figures_html}\n" + after
                else:
                    # Just replace the empty grid
                    new_content = content.replace(
                        '<div class="research-figures-grid">\n</div>',
                        figures_html
                    )
            else:
                # Add new figures section before publications
                if "## Related Publications" in content:
                    new_content = content.replace(
                        "## Related Publications", 
                        f"## Research Figures\n\n{figures_html}\n## Related Publications"
                    )
                else:
                    new_content = content + f"\n\n## Research Figures\n\n{figures_html}"
            
            # Write updated content
            with open(portfolio_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Updated Foundation Models portfolio with {len(figures)} custom figures")
            
        except Exception as e:
            print(f"❌ Error updating Foundation Models portfolio: {e}")

def main():
    creator = FoundationModelsFigureCreator()
    
    print("🎨 Creating custom figures for Foundation Models research...")
    
    # Create custom figures
    figures = []
    
    # AstroMLab figure
    astromlab_figure = creator.create_astromlab_logo_figure()
    figures.append(astromlab_figure)
    print(f"✅ Created AstroMLab figure: {astromlab_figure['filename']}")
    
    # EAIRA figure
    eaira_figure = creator.create_eaira_methodology_figure()
    figures.append(eaira_figure)
    print(f"✅ Created EAIRA figure: {eaira_figure['filename']}")
    
    # Update the portfolio
    creator.update_foundation_models_portfolio(figures)
    
    print(f"\n🎉 Successfully created {len(figures)} custom figures for Foundation Models!")
    print("\n💡 These custom figures provide visual representation for LLM research")
    print("   since Foundation Models papers typically don't contain extractable scientific figures.")

if __name__ == "__main__":
    main()