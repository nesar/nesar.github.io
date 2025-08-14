# Universal Website Content Manager

A generalized Python script to automatically manage academic website content for any researcher with publications on arXiv. The script uses LLM-based content generation to create research summaries, extract figures from papers, and maintain publication listings.

## Features

- **Researcher-Agnostic**: Works with any researcher by using configuration files
- **ArXiv Integration**: Automatically fetches publications from arXiv API
- **LLM-Powered**: Uses Google Gemini for intelligent content generation and paper classification
- **Figure Extraction**: Automatically extracts scientific figures from PDF papers
- **Research Categorization**: Dynamically groups papers into research themes
- **Portfolio Generation**: Creates detailed research portfolio pages
- **Jekyll Compatible**: Generates Jekyll-compatible markdown files

## Setup

1. **Install Dependencies**:
   ```bash
   pip install google-generativeai PyMuPDF Pillow numpy requests
   ```

2. **Get Google Gemini API Key**:
   - Visit: https://makersuite.google.com/app/apikey
   - Set environment variable: `export GEMINI_API_KEY='your-api-key-here'`

3. **Create Configuration File**:
   Copy `researcher_config.json` template and customize for your researcher

## Configuration

Create a JSON configuration file with the following structure:

```json
{
  "researcher": {
    "name": "Full Name",
    "title": "Dr.",
    "search_terms": [
      "au:\"Full Name\"",
      "au:\"Last, First\"",
      "au:\"F Last\""
    ],
    "author_patterns": [
      "(Last.*First)",
      "(Last.*F[\\s\\.])"
    ]
  },
  "website": {
    "base_dir": ".",
    "publications_dir": "_publications",
    "portfolio_dir": "_portfolio",
    "research_page": "_pages/research.html",
    "figures_dir": "images/research/figures",
    "papers_dir": "temp_papers"
  },
  "research_intro": "Research description paragraph...",
  "llm": {
    "api_key_env": "GEMINI_API_KEY",
    "model": "gemini-2.5-flash"
  }
}
```

### Configuration Fields

- **researcher.name**: Full name as it appears in publications
- **researcher.search_terms**: List of arXiv search queries to find papers
- **researcher.author_patterns**: Regex patterns to match author names (optional)
- **website.base_dir**: Base directory for website files
- **research_intro**: Introductory paragraph for research page
- **llm.api_key_env**: Environment variable name for API key
- **llm.model**: Gemini model to use

## Usage

### Basic Usage
```bash
# Full update with default config
python scripts/universal_website_content_manager.py --config researcher_config.json --full-update

# Research and portfolio only (preserve existing publications)
python scripts/universal_website_content_manager.py --config researcher_config.json --research-only
```

### Specific Updates
```bash
# Update publications only
python scripts/universal_website_content_manager.py --config researcher_config.json --update-publications

# Update research page only
python scripts/universal_website_content_manager.py --config researcher_config.json --update-research

# Update portfolio pages only
python scripts/universal_website_content_manager.py --config researcher_config.json --update-portfolio
```

## What It Creates

1. **Publication Files** (`_publications/`):
   - Individual markdown files for each paper
   - Jekyll front matter with metadata
   - arXiv links and citations

2. **Research Page** (`_pages/research.html`):
   - Dynamically categorized research overview
   - Extracted figures from papers
   - LLM-generated category summaries

3. **Portfolio Pages** (`_portfolio/`):
   - Detailed research area descriptions
   - Figure galleries
   - Interactive modals for images

4. **Figure Directory** (`images/research/figures/`):
   - High-quality scientific figures extracted from PDFs
   - Automatically named and organized

## Examples

See the included example configurations:
- `researcher_config.json` - Template for Nesar Ramachandra
- `example_researcher_config.json` - Example for a different researcher

## Customization Tips

1. **Search Terms**: Include all name variations your researcher uses
2. **Author Patterns**: Use regex for complex name matching
3. **Directory Structure**: Adjust paths to match your Jekyll site structure
4. **Research Introduction**: Write a compelling overview paragraph
5. **LLM Model**: Choose between different Gemini models based on needs

## Troubleshooting

- **No papers found**: Check search terms and author patterns
- **LLM errors**: Verify API key and network connection  
- **PDF download fails**: Some papers may have access restrictions
- **Figure extraction issues**: Requires PyMuPDF and valid PDF files

## Migration from Original Script

To migrate from the hardcoded `website_content_manager.py`:

1. Create a configuration file based on `researcher_config.json`
2. Update search terms and patterns for your specific researcher
3. Test with `--research-only` first to verify configuration
4. Run full update once everything works correctly