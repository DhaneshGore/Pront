# settings.py

import os

# Default configuration values
CONFIG = {
    "DEFAULT_LLM": "Google Gemini",  # Default model selection
    "HUGGINGFACE_API_URL": "https://api-inference.huggingface.co/models/facebook/bart-large-mnli",
}

# Function to get API key from environment variables (if set)
def get_api_key():
    return os.getenv("API_KEY", "")
