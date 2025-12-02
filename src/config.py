# Configuration for edu-ai-workflow-automation
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Main configuration class for the AI workflow automation system."""
    
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    MIDJOURNEY_API_KEY = os.getenv('MIDJOURNEY_API_KEY')
    
    # LLM Settings
    DEFAULT_LLM_MODEL = os.getenv('DEFAULT_LLM_MODEL', 'gpt-3.5-turbo')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 2000))
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    
    # Paths
    DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
    SAMPLES_DIR = os.path.join(DATA_DIR, 'samples')
    OUTPUTS_DIR = os.path.join(DATA_DIR, 'outputs')
    LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
    
    # Processing Settings
    MAX_FILE_SIZE_MB = int(os.getenv('MAX_FILE_SIZE_MB', 50))
    SUPPORTED_FILE_TYPES = ['pdf', 'txt', 'docx']
    
    # Quality Check Settings
    ENABLE_QUALITY_CHECK = os.getenv('ENABLE_QUALITY_CHECK', 'true').lower() == 'true'
    QUALITY_CHECK_MODEL = os.getenv('QUALITY_CHECK_MODEL', 'gpt-4')
    
    # Image Generation Settings
    IMAGE_GENERATION_MODEL = os.getenv('IMAGE_GENERATION_MODEL', 'dall-e-3')
    IMAGE_SIZE = os.getenv('IMAGE_SIZE', '1024x1024')
    
    # Layout Settings
    DEFAULT_TEMPLATE = os.getenv('DEFAULT_TEMPLATE', 'academic')
    SLIDE_FORMAT = os.getenv('SLIDE_FORMAT', 'pptx')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    ENABLE_EXPERIMENT_LOGGING = os.getenv('ENABLE_EXPERIMENT_LOGGING', 'true').lower() == 'true'
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present."""
        required_keys = ['OPENAI_API_KEY', 'GOOGLE_API_KEY']
        missing_keys = [key for key in required_keys if not getattr(cls, key)]
        
        if missing_keys:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_keys)}")
        
        return True