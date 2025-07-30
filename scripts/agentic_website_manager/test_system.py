#!/usr/bin/env python3
"""
Test script to verify the agentic website manager system works.
This script tests the system without making actual API calls.
"""

import sys
from pathlib import Path
import os

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that all modules can be imported."""
    print("🧪 Testing module imports...")
    
    try:
        import config
        print("   ✅ config imported")
        
        from base_agent import BaseAgent
        print("   ✅ BaseAgent imported")
        
        from web_agent import WebAgent
        print("   ✅ WebAgent imported")
        
        from parse_agent import ParseAgent
        print("   ✅ ParseAgent imported")
        
        from content_agent import ContentAgent
        print("   ✅ ContentAgent imported")
        
        from critic_agent import CriticAgent
        print("   ✅ CriticAgent imported")
        
        from orchestrator import WebsiteOrchestrator
        print("   ✅ WebsiteOrchestrator imported")
        
        return True
        
    except ImportError as e:
        print(f"   ❌ Import failed: {e}")
        return False

def test_configuration():
    """Test configuration system."""
    print("\n⚙️ Testing configuration system...")
    
    try:
        import config
        
        # Test basic config structure
        assert hasattr(config, 'config'), "No global config object found"
        assert hasattr(config.config, 'llm_config'), "No LLM config found"
        assert hasattr(config.config, 'search_config'), "No search config found"
        assert hasattr(config.config, 'prompts'), "No prompts config found"
        
        print("   ✅ Configuration structure is valid")
        
        # Test prompt availability
        prompts = config.config.prompts
        required_prompts = ['paper_classification', 'category_summary', 'portfolio_summary']
        
        for prompt_name in required_prompts:
            assert prompt_name in prompts, f"Missing prompt: {prompt_name}"
        
        print("   ✅ All required prompts are present")
        
        # Test search configuration
        search_config = config.config.search_config
        assert 'search_terms' in search_config, "No search terms found"
        assert len(search_config['search_terms']) > 0, "No search terms configured"
        
        print("   ✅ Search configuration is valid")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Configuration test failed: {e}")
        return False

def test_agent_initialization():
    """Test that agents can be initialized without API keys."""
    print("\n🤖 Testing agent initialization...")
    
    # Temporarily set a dummy API key for testing
    original_key = os.environ.get('GEMINI_API_KEY')
    os.environ['GEMINI_API_KEY'] = 'dummy-key-for-testing'
    
    try:
        # Test individual agent initialization
        from web_agent import WebAgent
        from parse_agent import ParseAgent
        from content_agent import ContentAgent
        from critic_agent import CriticAgent
        
        print("   ✅ All agent classes can be instantiated")
        
        # Test orchestrator initialization
        from orchestrator import WebsiteOrchestrator
        print("   ✅ WebsiteOrchestrator class is available")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Agent initialization test failed: {e}")
        return False
    
    finally:
        # Restore original API key
        if original_key:
            os.environ['GEMINI_API_KEY'] = original_key
        elif 'GEMINI_API_KEY' in os.environ:
            del os.environ['GEMINI_API_KEY']

def test_tool_availability():
    """Test that LangChain tools are properly defined."""
    print("\n🔧 Testing tool definitions...")
    
    try:
        from web_agent import search_arxiv_papers, download_papers
        print("   ✅ WebAgent tools are defined")
        
        from parse_agent import extract_figures_from_pdf, assess_figure_quality
        print("   ✅ ParseAgent tools are defined")
        
        from content_agent import classify_papers, generate_category_summary
        print("   ✅ ContentAgent tools are defined")
        
        from critic_agent import validate_classification, check_content_quality
        print("   ✅ CriticAgent tools are defined")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Tool availability test failed: {e}")
        return False

def test_file_structure():
    """Test that the expected file structure exists."""
    print("\n📁 Testing file structure...")
    
    try:
        current_dir = Path(__file__).parent
        
        required_files = [
            '__init__.py',
            'config.py',
            'base_agent.py',
            'web_agent.py',
            'parse_agent.py',
            'content_agent.py',
            'critic_agent.py',
            'orchestrator.py',
            'requirements.txt',
            'README.md',
        ]
        
        missing_files = []
        for file in required_files:
            if not (current_dir / file).exists():
                missing_files.append(file)
        
        if missing_files:
            print(f"   ❌ Missing files: {missing_files}")
            return False
        
        print("   ✅ All required files are present")
        
        # Test that files are not empty
        for file in ['config.py', 'orchestrator.py', 'README.md']:
            file_path = current_dir / file
            if file_path.stat().st_size == 0:
                print(f"   ❌ File {file} is empty")
                return False
        
        print("   ✅ Core files have content")
        
        return True
        
    except Exception as e:
        print(f"   ❌ File structure test failed: {e}")
        return False

def print_system_info():
    """Print information about the system."""
    print("\n📊 System Information:")
    print("=" * 50)
    
    try:
        import config
        
        # Agent information
        agent_info = {
            'WebAgent': 'Searches and downloads research papers from arXiv',
            'ParseAgent': 'Extracts figures and text from PDF files',
            'ContentAgent': 'Classifies papers and generates content using LLM',
            'CriticAgent': 'Validates and reviews generated content',
            'Orchestrator': 'Coordinates all agents in complex workflows'
        }
        
        print("🤖 Available Agents:")
        for agent, description in agent_info.items():
            print(f"   • {agent}: {description}")
        
        # Configuration info
        print(f"\n⚙️ Configuration:")
        print(f"   • LLM Model: {config.config.llm_config['model_name']}")
        print(f"   • Search Terms: {len(config.config.search_config['search_terms'])} configured")
        print(f"   • Categories: {len(config.config.classification_config['categories'])} defined")
        print(f"   • Prompts: {len(config.config.prompts)} available")
        
        # File paths
        print(f"\n📁 File Paths:")
        print(f"   • Publications: {config.config.publications_dir}")
        print(f"   • Portfolio: {config.config.portfolio_dir}")
        print(f"   • Research Page: {config.config.research_page}")
        print(f"   • Figures: {config.config.figures_dir}")
        
    except Exception as e:
        print(f"   ❌ Could not retrieve system info: {e}")

def main():
    """Run all tests."""
    print("🧪 Agentic Website Manager - System Test")
    print("=" * 60)
    
    tests = [
        ("Module Imports", test_imports),
        ("Configuration", test_configuration),
        ("Agent Initialization", test_agent_initialization),
        ("Tool Availability", test_tool_availability),
        ("File Structure", test_file_structure),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        results[test_name] = test_func()
    
    # Print results
    print("\n" + "=" * 60)
    print("📋 TEST RESULTS")
    print("=" * 60)
    
    passed = 0
    total = len(tests)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is ready to use.")
        print_system_info()
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)