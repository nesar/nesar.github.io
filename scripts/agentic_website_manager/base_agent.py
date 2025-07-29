"""
Base Agent class for all specialized agents.
Uses LangChain for agent orchestration and provides common functionality.
"""

import os
import time
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
import google.generativeai as genai
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import BaseTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema import AgentAction, AgentFinish

from .config import config

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """
    Base class for all agents providing common LLM functionality and structure.
    """
    
    def __init__(self, name: str, description: str, tools: List[BaseTool] = None):
        self.name = name
        self.description = description
        self.tools = tools or []
        self.llm = None
        self.agent_executor = None
        self.setup_llm()
        
    def setup_llm(self):
        """Setup LLM with error handling."""
        api_key = config.llm_config['api_key_env']
        api_key_value = os.getenv(api_key)
        
        if not api_key_value:
            logger.error(f"❌ {api_key} environment variable is required.")
            logger.error("   Get your API key from: https://makersuite.google.com/app/apikey")
            logger.error(f"   Then set it: export {api_key}='your-api-key-here'")
            raise ValueError(f"Missing {api_key} environment variable")
        
        try:
            # Setup direct Gemini client for simple calls
            genai.configure(api_key=api_key_value)
            self.direct_model = genai.GenerativeModel(config.llm_config['model_name'])
            
            # Setup LangChain LLM for agent orchestration
            self.llm = ChatGoogleGenerativeAI(
                model=config.llm_config['model_name'],
                google_api_key=api_key_value,
                temperature=0.1
            )
            
            logger.info(f"✅ LLM configured successfully for {self.name}")
            
        except Exception as e:
            logger.error(f"❌ LLM setup failed for {self.name}: {e}")
            raise
    
    def llm_generate(self, prompt: str, max_retries: int = None) -> str:
        """Generate content using direct LLM with retry logic."""
        max_retries = max_retries or config.llm_config['max_retries']
        
        for attempt in range(max_retries):
            try:
                response = self.direct_model.generate_content(prompt)
                return response.text.strip()
            except Exception as e:
                logger.warning(f"⚠️ LLM attempt {attempt + 1} failed for {self.name}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(config.llm_config['retry_backoff'] ** attempt)
                else:
                    raise
    
    def create_agent_executor(self, prompt_template: str) -> AgentExecutor:
        """Create LangChain agent executor with tools."""
        if not self.tools:
            logger.warning(f"No tools provided for {self.name}")
            return None
            
        prompt = PromptTemplate.from_template(prompt_template)
        
        # Create ReAct agent
        agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )
        
        # Create agent executor
        agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=5
        )
        
        return agent_executor
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Dict[str, Any]:
        """Execute the agent's main task. Must be implemented by subclasses."""
        pass
    
    def validate_inputs(self, inputs: Dict[str, Any], required_keys: List[str]) -> bool:
        """Validate that all required inputs are present."""
        missing_keys = [key for key in required_keys if key not in inputs]
        if missing_keys:
            logger.error(f"❌ Missing required inputs for {self.name}: {missing_keys}")
            return False
        return True
    
    def log_start(self, task_description: str):
        """Log the start of an agent task."""
        logger.info(f"🤖 {self.name}: Starting {task_description}")
    
    def log_success(self, task_description: str, details: str = ""):
        """Log successful completion of an agent task."""
        message = f"✅ {self.name}: Completed {task_description}"
        if details:
            message += f" - {details}"
        logger.info(message)
    
    def log_error(self, task_description: str, error: Exception):
        """Log an error in agent execution."""
        logger.error(f"❌ {self.name}: Failed {task_description} - {str(error)}")