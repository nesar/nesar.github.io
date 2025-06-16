# Website Content Management

Clean, unified script system for maintaining the research website.

## Files

- `website_content_manager.py` - **Main script** (does everything)
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r scripts/requirements.txt
   ```

2. **Get Gemini API key:**
   - Visit: https://makersuite.google.com/app/apikey
   - Set environment variable: `export GEMINI_API_KEY='your-key-here'`

## Usage

```bash
# Update entire website (recommended)
python scripts/website_content_manager.py

# Or update specific components
python scripts/website_content_manager.py --update-publications
python scripts/website_content_manager.py --update-research  
python scripts/website_content_manager.py --update-portfolio
```

## What It Does

1. **Fetches publications** from arXiv automatically
2. **Classifies papers** into research categories using LLM
3. **Downloads papers** and extracts best scientific figures
4. **Generates summaries** and content using LLM
5. **Creates pages** with clean, responsive HTML

## Key Features

✅ **Fully automated** - No manual paper categorization  
✅ **LLM-powered** - Intelligent content generation  
✅ **Clean output** - Consistent formatting  
✅ **Single script** - Replaces multiple legacy scripts

## Output Files

- `_publications/` - Publication markdown files
- `_pages/research.html` - Research overview page  
- `_portfolio/` - Research area portfolio pages
- `images/research/figures/` - Extracted scientific figures
- `temp_papers/` - Downloaded PDF files