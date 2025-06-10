# Website Automation Scripts

This directory contains automation scripts for maintaining Nesar Ramachandra's academic website.

## Scripts Overview

### 1. `automated_update.py` - Main Automation Tool

This is the primary script for managing publications and research content.

**Usage:**
```bash
# List all current publications
python scripts/automated_update.py list

# Clean duplicate publications  
python scripts/automated_update.py clean

# Update research portfolio based on publications
python scripts/automated_update.py update-research

# Extract figures from papers and add to research pages
python scripts/automated_update.py extract-figures

# Run complete update (clean + research + figures)
python scripts/automated_update.py full-update

# Add a publication manually
python scripts/automated_update.py add-manual \
  --title "Paper Title" \
  --authors "Author 1, Author 2" \
  --venue "Journal Name" \
  --date "2024-01-01" \
  --url "https://arxiv.org/abs/..." \
  --abstract "Abstract text here"
```

### 2. `validate_site.py` - Site Structure Validator

Validates Jekyll site structure and YAML front matter.

**Usage:**
```bash
python scripts/validate_site.py
```

### 3. `daily_update.py` - Daily Automation

Runs all automation tasks in sequence. Ideal for regular maintenance.

**Usage:**
```bash
python scripts/daily_update.py
```

### 4. `extract_figures.py` - Figure Extraction Tool

Extracts high-quality figures from academic papers and adds them to research pages.

**Usage:**
```bash
# Extract figures from a local PDF
python scripts/extract_figures.py extract-local \
  --pdf "path/to/paper.pdf" \
  --title "Paper Title"

# Extract figures from an online PDF/arXiv URL
python scripts/extract_figures.py extract-url \
  --url "https://arxiv.org/abs/2303.16869" \
  --title "Paper Title"
```

**Features:**
- Automatically downloads PDFs from arXiv URLs
- Filters figures by quality (size, complexity, aspect ratio)
- Categorizes figures by research area
- Creates interactive galleries with modal popups
- Avoids extracting low-quality or AI-generated images

### 5. `auto_extract_from_publications.py` - Batch Figure Extraction

Automatically processes existing publications to extract figures.

### 6. Legacy Scripts

- `update_publications.py` - Original arXiv-based updater
- `update_scholar_publications.py` - Google Scholar-based updater  
- `update_publications_improved.py` - Enhanced API-based updater
- `update_research.py` - Research portfolio generator

## Automation Workflow

### Daily Maintenance (Recommended)

1. Run the daily automation:
   ```bash
   python scripts/daily_update.py
   ```

2. Review the generated `publication_list.txt`

3. Test locally:
   ```bash
   bundle exec jekyll serve
   ```

4. Commit and push changes:
   ```bash
   git add .
   git commit -m "Automated website update"
   git push
   ```

### Manual Publication Updates

When you have new publications:

1. Add them manually:
   ```bash
   python scripts/automated_update.py add-manual \
     --title "Your New Paper" \
     --authors "You, Coauthor" \
     --venue "Amazing Journal" \
     --date "2024-12-01" \
     --url "https://doi.org/10.1000/xyz"
   ```

2. Update research portfolio:
   ```bash
   python scripts/automated_update.py update-research
   ```

### Site Customization

The website aesthetics are controlled by:
- `assets/css/custom.css` - Custom styling for modern, crisp look
- `_data/navigation.yml` - Navigation menu structure
- `_config.yml` - Site configuration

### Research Categories

Publications and figures are automatically categorized into:
- **Machine Learning & AI** - ML, deep learning, neural networks
- **Dark Matter & Cosmology** - Cosmic web, dark matter, cosmology
- **Uncertainty Quantification** - Bayesian methods, probabilistic modeling  
- **Gravitational Lensing** - Strong/weak lensing studies
- **Other Research** - Everything else

### Figure Quality Criteria

The system automatically selects high-quality figures by:
- **Size filtering**: Minimum 300x200 pixels, avoiding tiny images
- **Aspect ratio**: Excludes very wide/thin images (likely headers/footers)
- **Color complexity**: Ensures sufficient visual complexity
- **File size**: Between 10KB-2MB to avoid simple graphics or huge images
- **Content filtering**: Avoids extracting text-only or simple diagrams

## Troubleshooting

### Common Issues

1. **Duplicate Publications**: Run `python scripts/automated_update.py clean`

2. **YAML Errors**: Run `python scripts/validate_site.py` to identify issues

3. **Missing Dependencies**: Install required packages:
   ```bash
   pip install requests pyyaml scholarly
   ```

4. **Jekyll Build Errors**: Check that all markdown files have valid YAML front matter

### File Structure

```
scripts/
├── README.md                          # This file
├── automated_update.py                # Main automation tool
├── daily_update.py                   # Daily automation runner
├── validate_site.py                  # Site validator
├── update_publications_improved.py   # Enhanced publication updater
└── [legacy scripts...]              # Older automation scripts
```

## Future Enhancements

Potential improvements:
1. GitHub Actions integration for automatic updates
2. API integration with NASA ADS for astrophysics papers
3. ORCID integration for publication verification
4. Automated citation count updates
5. Research impact metrics tracking

## Support

For issues or questions:
1. Check this README
2. Run the validation script to identify problems
3. Review Jekyll error messages
4. Check file permissions and dependencies