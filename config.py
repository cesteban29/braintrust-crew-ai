import os
from dotenv import load_dotenv

load_dotenv()

BRAINTRUST_API_KEY = os.getenv("BRAINTRUST_API_KEY")
BRAINTRUST_PROJECT = os.getenv("BRAINTRUST_PROJECT", "crew-ai-project")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if BRAINTRUST_API_KEY:
    os.environ["BRAINTRUST_API_KEY"] = BRAINTRUST_API_KEY
if BRAINTRUST_PROJECT:
    os.environ["BRAINTRUST_PARENT"] = f"project_name:{BRAINTRUST_PROJECT}"
if OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
if SERPER_API_KEY:
    os.environ["SERPER_API_KEY"] = SERPER_API_KEY

def validate_config():
    """Validate that all required environment variables are set."""
    missing = []
    if not BRAINTRUST_API_KEY:
        missing.append("BRAINTRUST_API_KEY")
    if not OPENAI_API_KEY:
        missing.append("OPENAI_API_KEY")
    if not SERPER_API_KEY:
        missing.append("SERPER_API_KEY")
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}. "
                        f"Please set them in your .env file or environment.")
    
    return True