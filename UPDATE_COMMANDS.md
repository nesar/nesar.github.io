# Website Update Commands

This guide contains all the commands you need to update your clean, optimized academic website.

> **Note**: The codebase has been cleaned up - removed 20+ unnecessary template files, unused layouts, demo content, and duplicate files. See `STRUCTURE.md` for full details.

## Quick Update (Recommended)

For a complete website refresh with latest publications and clean organization:

```bash
cd /Users/nesar/Projects/Misc/nesar.github.io
python3 scripts/cleanup_and_organize.py
```

This single command will:
- ✅ Refresh research images by extracting figures from papers
- ✅ Update publications page with single Paper link logic
- ✅ Analyze all 60+ publications and categorize them correctly
- ✅ Ensure exhaustive publication lists for each research area
- ✅ Select diverse figures from different papers (max 2 per category)
- ✅ Create clean portfolio pages without duplicates
- ✅ Generate a clean research overview page
- ✅ Fix any content issues automatically

## Individual Update Commands

### 1. Refresh Research Images Only

If you just want to update the research figures:

```bash
# Auto-extract figures from all publications
python3 scripts/auto_extract_from_publications.py

# Extract figures from a specific PDF
python3 scripts/extract_figures.py /path/to/new_paper.pdf
```

### 2. Update Publications Data

To fetch latest publications from Google Scholar/arXiv:

```bash
python3 scripts/update_scholar_publications.py
```

### 3. Validate Website Structure

To check for issues without making changes:

```bash
# Check for duplicate content
grep -r "Machine Learning & AI" _portfolio/ _pages/

# Count publications per category
python3 -c "
import os, re
from collections import defaultdict

categories = defaultdict(int)
for f in os.listdir('_publications'):
    if f.endswith('.md'):
        with open(f'_publications/{f}', 'r') as file:
            content = file.read()
            if any(k in content.lower() for k in ['machine learning', 'deep learning', 'ai ']):
                categories['ML'] += 1
            elif any(k in content.lower() for k in ['dark matter', 'cosmic web', 'cosmology']):
                categories['Dark Matter'] += 1
            elif any(k in content.lower() for k in ['uncertainty', 'probabilistic']):
                categories['UQ'] += 1
            elif any(k in content.lower() for k in ['emulator', 'surrogate']):
                categories['Emulation'] += 1

for cat, count in categories.items():
    print(f'{cat}: {count} papers')
"
```

## Testing Locally

Before deploying changes:

```bash
# Install Jekyll dependencies (one-time setup)
bundle install

# Serve locally
bundle exec jekyll serve

# View at: http://localhost:4000
```

## Deployment

Your website auto-deploys via GitHub Pages when you push to master:

```bash
git add .
git commit -m "Update research content and figures"
git push origin master
```

## File Structure Reference

```
_portfolio/
├── portfolio-1-machine-learning.md       # 24 ML papers
├── portfolio-2-dark-matter.md           # 10 Dark Matter papers  
├── portfolio-3-uncertainty-quantification.md  # 4 UQ papers
└── portfolio-4-statistical-emulation.md # 10 Statistical Emulation papers

_pages/
└── research.html                         # Clean overview page

images/research/figures/                  # Extracted figures
scripts/
├── cleanup_and_organize.py              # Main update script
├── extract_figures.py                   # Figure extraction
└── update_scholar_publications.py       # Publication updates
```

## Troubleshooting

### If figures aren't showing:
```bash
# Check if figure files exist
ls -la images/research/figures/

# Regenerate figures
python3 scripts/extract_figures.py
```

### If duplicates appear:
```bash
# Run cleanup (fixes all duplicates)
python3 scripts/cleanup_and_organize.py
```

### If publication counts are wrong:
```bash
# Force refresh all publications
python3 scripts/cleanup_and_organize.py
```

## Automation Schedule

For regular updates, you can set up a cron job:

```bash
# Edit crontab
crontab -e

# Add line for monthly updates (runs 1st of each month at 9 AM)
0 9 1 * * cd /Users/nesar/Projects/Misc/nesar.github.io && python3 scripts/cleanup_and_organize.py
```

## Current Status

After running `cleanup_and_organize.py`, your website has:
- ✅ **Foundation Models**: LLM and foundation model research, 2 figures
- ✅ **Machine Learning for Science**: Non-LLM ML applications, 2 figures
- ✅ **Dark Matter & Cosmology**: Cosmological simulations, 2 figures  
- ✅ **Emulation & Inference**: Combined UQ and emulation methods, 2 figures
- ✅ Clean research overview with no duplicates
- ✅ Single "Paper" links (published version or arXiv fallback)
- ✅ Publications properly categorized by research area

## Support

If you encounter issues:
1. Check this file for relevant commands
2. Run `python3 scripts/cleanup_and_organize.py` to fix most problems
3. Check the console output for specific error messages