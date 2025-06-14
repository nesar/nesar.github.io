# Research Website Scripts

This directory contains the essential scripts for maintaining the research website.

## Core Scripts

### `research_overhaul.py`
**Main research page generator**
- Classifies papers into 4 research categories
- Generates research summaries (with optional Gemini LLM integration)
- Creates a professional research page with clean UI
- Run this to completely rebuild the research page

**Usage:**
```bash
python scripts/research_overhaul.py
```

### `extract_plots_direct.py`
**Scientific figure extractor**
- Extracts high-quality scientific figures from PDF papers
- Selects the best/last plots from each paper (usually the best results)
- Updates the research page with real scientific figures
- Run this after having PDFs in temp_papers/ directory

**Usage:**
```bash
python scripts/extract_plots_direct.py
```

### `update_publications_improved.py`
**Publication page updater**
- Maintains the publications page
- Updates citation counts and metadata
- Keeps publication listings current

**Usage:**
```bash
python scripts/update_publications_improved.py
```

## Setup Scripts

### `setup_gemini.py`
**Optional LLM integration setup**
- Configures Gemini API for better research summaries
- Optional - the main script works with fallback summaries
- Only needed if you want LLM-generated category descriptions

**Usage:**
```bash
python scripts/setup_gemini.py
```

### `requirements.txt`
**Package dependencies**
- Lists all required Python packages
- Install with: `pip install -r scripts/requirements.txt`

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r scripts/requirements.txt
   ```

2. **Complete research page overhaul:**
   ```bash
   python scripts/research_overhaul.py
   python scripts/extract_plots_direct.py
   ```

3. **Update publications:**
   ```bash
   python scripts/update_publications_improved.py
   ```

## Files Structure

- `temp_papers/` - Place PDF files here for figure extraction
- `images/research/figures/` - Extracted scientific figures stored here
- `_pages/research.html` - Generated research page
- `_publications/` - Publication metadata files

## Notes

- The research overhaul script automatically classifies 56+ papers into 4 categories
- Figure extraction works best with PDFs that have embedded images
- Research page features responsive design and modal image viewing
- All figures extracted are high-quality scientific visualizations from actual papers