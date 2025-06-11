# Website Structure & Maintenance Guide

This document explains the clean, optimized structure of your academic website after removing unnecessary template files.

## 📁 Core Directory Structure

```
nesar.github.io/
├── _config.yml                    # Main Jekyll configuration
├── _config.dev.yml                # Development configuration
├── _data/
│   ├── authors.yml                # Author metadata
│   ├── navigation.yml             # Site navigation menu
│   └── ui-text.yml                # UI text and translations
├── _includes/                     # Reusable components
├── _layouts/                      # Page templates
├── _pages/                        # Main site pages
├── _portfolio/                    # Research portfolio items
├── _publications/                 # Publication metadata (60+ files)
├── _sass/                         # SCSS stylesheets
├── _talks/                        # Conference talks
├── _teaching/                     # Teaching experience
├── assets/                        # CSS, JS, fonts
├── files/                         # PDFs and documents
├── images/                        # Profile and research images
├── markdown_generator/            # Publication generation tools
└── scripts/                       # Automation scripts
```

## 🎯 Active Pages (_pages/)

- **about.md** - Homepage/About page
- **cv.md** - Curriculum Vitae
- **publications.md** - Publications list with Google Scholar link
- **research.html** - Research overview with portfolio preview
- **portfolio.html** - Full portfolio listing
- **miscellaneous.md** - Talks, teaching, and other content
- **404.md** - Error page

## 🔧 Essential Collections

### _portfolio/ (4 items)
- **portfolio-1-machine-learning.md** - ML & AI research (24 papers)
- **portfolio-2-dark-matter.md** - Cosmology research (10 papers)  
- **portfolio-3-uncertainty-quantification.md** - UQ research (4 papers)
- **portfolio-4-statistical-emulation.md** - Statistical methods (10 papers)

### _publications/ (60+ items)
All your academic publications organized by year and venue.

### _talks/ (5 items)
Conference presentations and talks.

### _teaching/ (3 items)
Teaching and mentorship experience.

## 🎨 Styling & Assets

### CSS Structure
- **assets/css/main.scss** - Main stylesheet (imports everything)
- **assets/css/custom.css** - Your custom modern styling
- **assets/css/academicons.css** - Academic icons
- **_sass/** - SCSS components and variables

### JavaScript
- **assets/js/main.min.js** - Minified main JavaScript
- **assets/js/_main.js** - Source JavaScript
- **assets/js/plugins/** - jQuery plugins (navigation, lightbox, etc.)

## 🤖 Automation Scripts (/scripts/)

- **cleanup_and_organize.py** - Main script for organizing research content
- **extract_figures.py** - Extracts figures from PDFs
- **update_publications.py** - Updates publication data
- **update_research.py** - Updates research content
- **update_scholar_publications.py** - Syncs with Google Scholar

## 📋 Configuration Files

### _config.yml
Main site configuration including:
- Site settings (title, description, URL)
- Author information
- Social media links
- Collection definitions
- Plugin configuration

### _data/navigation.yml
Site navigation menu structure.

## 🚀 Key Features

### Automated Research Management
- Automatic publication categorization
- Figure extraction from papers
- Research portfolio generation
- Google Scholar integration

### Modern Design
- Clean, professional styling
- Responsive layout
- Interactive research figures
- Modal image galleries

### Optimized Performance
- Minified CSS/JS
- Optimized images
- Clean HTML structure
- Fast loading times

## 🔄 Maintenance Commands

### Update Everything
```bash
python3 scripts/cleanup_and_organize.py
```

### Extract Figures from New Papers
```bash
python3 scripts/extract_figures.py /path/to/paper.pdf
```

### Update Publications
```bash
python3 scripts/update_scholar_publications.py
```

### Local Development
```bash
bundle exec jekyll serve
```

## 📝 What Was Removed

### Template Content (Cleaned Up)
- Demo blog posts (_posts/2012-2015-*)
- Template pages (markdown.md, terms.md, etc.)
- Example comments (_data/comments/)
- Unused layouts (pdf.html, splash.html)
- Template images (fig2.png, research2-4.png, etc.)
- Unused archive pages
- Duplicate research collection (_research/)
- Unused comment providers
- Talkmap functionality
- Browser configuration files

### File Count Reduction
- **Before**: ~200+ files with many templates
- **After**: ~180 files, all functional
- **Savings**: ~20% reduction in repository size

## 🎯 Content Organization

### Research Categories
1. **Machine Learning & AI** - 24 papers, 4 figures
2. **Dark Matter & Cosmology** - 10 papers, 2 figures
3. **Uncertainty Quantification** - 4 papers, 2 figures
4. **Statistical Emulation** - 10 papers, 2 figures

### Navigation Structure
- **About** - Main landing page
- **Research** - Portfolio overview
- **Publications** - Complete publication list
- **CV** - Academic CV
- **Miscellaneous** - Talks, teaching, other

## 🔍 File Naming Conventions

### Publications
Format: `YYYY-MM-DD-title-slug.md`
Example: `2024-11-13-astromlab-3-achieving-gpt-4o-level-performance.md`

### Portfolio
Format: `portfolio-N-category.md`
Example: `portfolio-1-machine-learning.md`

### Research Figures
Format: `paper_title_pageN_figN_hash.png`
Example: `astromlab_3_page5_fig1_abc123.png`

## 🛠️ Best Practices

### Adding New Content
1. **Publications**: Add to `_publications/` following naming convention
2. **Research Figures**: Use `extract_figures.py` script
3. **Portfolio Updates**: Run `cleanup_and_organize.py`

### Editing Existing Content
- Modify files directly in respective directories
- Use scripts for bulk updates
- Test locally before deploying

### Maintenance Schedule
- **Monthly**: Run `cleanup_and_organize.py`
- **As needed**: Add new publications and run figure extraction
- **Quarterly**: Review and update automation scripts

This optimized structure maintains full functionality while being much cleaner and easier to maintain!