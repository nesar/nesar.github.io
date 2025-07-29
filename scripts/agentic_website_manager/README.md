# Agentic Website Manager

A modular AI-powered system for automatically managing research website content using specialized agents and LLM orchestration.

## Overview

This system replaces the monolithic `website_content_manager.py` with a modular, agent-based architecture that provides the same functionality but with better organization, maintainability, and extensibility.

## Architecture

The system consists of four specialized agents:

### 🕷️ WebAgent
- **Purpose**: Web searching and paper downloading
- **Tools**: arXiv API search, PDF downloading, rate limiting
- **Output**: List of papers with metadata and local file paths

### 🔍 ParseAgent  
- **Purpose**: PDF processing and figure extraction
- **Tools**: PDF text extraction, figure quality assessment, image processing
- **Output**: Extracted figures, text content, and metadata

### 📝 ContentAgent
- **Purpose**: Paper classification and content generation
- **Tools**: LLM-based classification, summary generation, HTML creation
- **Output**: Research categories, summaries, and formatted content

### 🔍 CriticAgent
- **Purpose**: Validation and quality assurance
- **Tools**: Classification validation, content quality checks, consistency analysis
- **Output**: Validation reports and recommendations

### 🎯 Orchestrator
- **Purpose**: Coordinates all agents in complex workflows
- **Features**: Pipeline management, error handling, progress tracking

## Key Features

### ✅ Modular Design
- Each agent has a single responsibility
- Easy to modify, extend, or replace individual components
- Clear interfaces between agents

### ✅ Configuration Management
- All prompts, settings, and configurations in `config.py`
- Easy to customize for different users or use cases
- No hardcoded values throughout the system

### ✅ LangChain Integration
- Uses LangChain for agent orchestration
- ReAct agents with tool access
- Structured agent communication

### ✅ Comprehensive Validation
- Automatic quality checks on all generated content
- Classification accuracy validation
- Data consistency verification
- Detailed reporting

### ✅ Error Handling & Logging
- Robust error handling at every stage
- Detailed logging and progress tracking
- Graceful degradation when components fail

### ✅ Portability
- Self-contained package structure
- Clear dependency management
- Easy to deploy to different environments

## Installation

1. **Install dependencies:**
   ```bash
   cd scripts/agentic_website_manager
   pip install -r requirements.txt
   ```

2. **Set up API keys:**
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key"
   ```

3. **Verify installation:**
   ```bash
   python orchestrator.py --help
   ```

## Usage

### Command Line Interface

```bash
# Full website update (publications + research + portfolio)
python orchestrator.py --full-update

# Research and portfolio only (preserve existing publications)
python orchestrator.py --research-only

# Skip validation checks (faster)
python orchestrator.py --full-update --no-validation
```

### Python API

```python
from agentic_website_manager import WebsiteOrchestrator

# Initialize orchestrator
orchestrator = WebsiteOrchestrator()

# Run full pipeline
results = orchestrator.run_full_pipeline(validate=True)

# Research-only update
results = orchestrator.run_research_only_update(validate=True)

# Check results
if results['success']:
    print(f"Processed {results['final_results']['papers_processed']} papers")
    print(f"Generated {results['final_results']['categories_created']} categories")
else:
    print(f"Pipeline failed: {results['error']}")
```

### Individual Agent Usage

```python
from agentic_website_manager import WebAgent, ParseAgent, ContentAgent, CriticAgent

# Use individual agents
web_agent = WebAgent()
papers = web_agent.execute("search_and_download")

parse_agent = ParseAgent()
figures = parse_agent.execute(papers['papers'], "extract_figures")

content_agent = ContentAgent()
content = content_agent.execute(papers['papers'], figures['figures_extracted'])

critic_agent = CriticAgent()
validation = critic_agent.execute({
    'papers': papers['papers'],
    'categories': content['categories'],
    'figures': figures['figures_extracted']
})
```

## Configuration

### Customizing Prompts
Edit `config.py` to modify LLM prompts:

```python
config.prompts['paper_classification'] = """
Your custom classification prompt here...
{paper_list}
"""
```

### Search Configuration
Modify search terms and parameters:

```python
config.search_config['search_terms'] = [
    'au:"Your Name"',
    'au:"Name, Your"'
]
```

### Classification Categories
Customize research categories:

```python
config.classification_config['categories']['new-category'] = {
    'name': 'New Research Area',
    'description': 'Description of the research area',
    'keywords': ['keyword1', 'keyword2']
}
```

## File Structure

```
agentic_website_manager/
├── __init__.py           # Package initialization
├── config.py             # All configuration and prompts
├── base_agent.py         # Base agent class
├── web_agent.py          # Web search and download agent
├── parse_agent.py        # PDF parsing and figure extraction
├── content_agent.py      # Content classification and generation
├── critic_agent.py       # Validation and quality assurance
├── orchestrator.py       # Main coordination and CLI
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## Extending the System

### Adding New Agents
1. Inherit from `BaseAgent`
2. Define tools using `@tool` decorator
3. Implement `execute()` method
4. Add to orchestrator workflow

### Adding New Tools
```python
from langchain.tools import tool

@tool
def your_custom_tool(input_param: str) -> str:
    """Description of what your tool does."""
    # Tool implementation
    return result
```

### Custom Workflows
```python
# Create custom orchestration
def custom_workflow():
    web_agent = WebAgent()  
    # ... custom logic
    return results
```

## Validation and Quality Checks

The system includes comprehensive validation:

- **Classification Validation**: Ensures all papers are properly categorized
- **Content Quality**: Checks HTML/Markdown formatting and completeness  
- **Data Consistency**: Verifies cross-references between papers, categories, and figures
- **Error Reporting**: Detailed reports with recommendations

## Comparison with Original System

| Feature | Original | Agentic System |
|---------|----------|----------------|
| Architecture | Monolithic | Modular agents |
| Configuration | Hardcoded | Centralized config |  
| Validation | Basic | Comprehensive |
| Extensibility | Limited | Highly extensible |
| Error Handling | Basic | Robust |
| Testing | Difficult | Agent-level testing |
| Maintainability | Low | High |

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure `GEMINI_API_KEY` is set
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **Permission Errors**: Check file system permissions
4. **Network Issues**: Check internet connection for arXiv access

### Debug Mode
Enable verbose logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Validation Failures
Run with validation to identify issues:
```bash
python orchestrator.py --full-update  # validation enabled by default
```

## License

This system is designed to be portable and can be easily adapted for different users and use cases. The modular architecture ensures that individual components can be modified or replaced without affecting the entire system.

## Future Enhancements

- Support for additional paper sources (PubMed, IEEE, etc.)
- Advanced figure analysis and captioning
- Multi-language support
- Integration with citation managers
- Real-time content updates
- Web dashboard for monitoring and control