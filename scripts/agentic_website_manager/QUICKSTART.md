# Agentic Website Manager - Quick Start Guide

## 🚀 Quick Setup

1. **Navigate to the directory:**
   ```bash
   cd scripts/agentic_website_manager
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key-here"
   ```

4. **Test the system:**
   ```bash
   python test_system.py
   ```

5. **Run the system:**
   ```bash
   # Full update (publications + research + portfolio)
   python run.py --full-update

   # Research and portfolio only (preserve existing publications)
   python run.py --research-only

   # Skip validation for faster execution
   python run.py --full-update --no-validation
   ```

## 🎯 What This System Does

The Agentic Website Manager is a modular replacement for the original `website_content_manager.py` that:

- **🕷️ WebAgent**: Searches arXiv for your papers and downloads PDFs
- **🔍 ParseAgent**: Extracts figures and text from research papers
- **📝 ContentAgent**: Classifies papers into categories and generates summaries
- **🔍 CriticAgent**: Validates all work for quality and consistency
- **🎯 Orchestrator**: Coordinates everything in smooth workflows

## ⚙️ Customization

### Edit Search Terms
In `config.py`, modify:
```python
config.search_config['search_terms'] = [
    'au:"Your Name"',
    'au:"Name, Your"'
]
```

### Customize Research Categories
In `config.py`, modify:
```python
config.classification_config['categories']['new-category'] = {
    'name': 'New Research Area',
    'description': 'Description',
    'keywords': ['keyword1', 'keyword2']
}
```

### Edit LLM Prompts
In `config.py`, modify:
```python
config.prompts['paper_classification'] = """
Your custom prompt here...
"""
```

## 🔧 Troubleshooting

### Common Issues:

1. **Import errors**: Make sure you're in the right directory and dependencies are installed
2. **API key error**: Ensure `GEMINI_API_KEY` environment variable is set
3. **Permission errors**: Check file system permissions for writing to directories

### Debug Mode:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📊 System Architecture

```
WebAgent → ParseAgent → ContentAgent → CriticAgent
    ↓         ↓           ↓             ↓
  Papers → Figures → Categories → Validation
```

All coordinated by the **Orchestrator** which handles:
- Pipeline execution
- Error handling  
- Progress tracking
- File writing

## 🎉 Success!

If the test passes, your system is ready to automatically:
- Find and download your research papers
- Extract scientific figures
- Classify papers into research areas
- Generate beautiful research page content
- Create detailed portfolio pages
- Validate everything for quality

**Enjoy your automated website management! 🚀**