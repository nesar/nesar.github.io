# Website Automation Scripts

This directory contains scripts for automating the maintenance of the personal website.

## Scripts

- `update_publications.py`: Automatically fetches publications from arXiv and ADS and creates or updates the corresponding markdown files.
- `update_research.py`: Analyzes publication content to extract research themes and generates portfolio items.

## Usage

These scripts are automatically run via GitHub Actions workflows defined in the `.github/workflows` directory. The workflows are scheduled to run periodically but can also be triggered manually.

### Manual Execution

To run these scripts manually:

1. Make sure you have the required dependencies installed:
   ```
   pip install requests scholarly pyyaml scikit-learn nltk
   ```

2. Run the scripts in the following order:
   ```
   python update_publications.py
   python update_research.py
   ```

## Configuration

Each script has configuration variables at the top that can be modified:

- `AUTHOR_NAME`: Your name as it appears in publications
- `ARXIV_SEARCH_QUERY`: Your arXiv search query
- `RESEARCH_THEMES`: Dictionary mapping research theme keywords to relevant terms

## Adding New Automation Features

To add new automation features:

1. Create a new Python script in this directory
2. Add a corresponding GitHub Actions workflow in `.github/workflows/`
3. Update this README with information about the new script
