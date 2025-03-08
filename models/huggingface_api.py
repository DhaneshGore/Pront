# huggingface_api.py

import requests
from settings import CONFIG

def query_huggingface(api_key, model, prompt):
    """Query the Hugging Face API for text generation or enhancement."""
    headers = {"Authorization": f"Bearer {api_key}"}
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

def analyze_prompt_hf(api_key, prompt):
    """Analyze a prompt using a Hugging Face model."""
    model = "facebook/bart-large-mnli"  # Example model
    return query_huggingface(api_key, model, prompt)

def enhance_prompt_hf(api_key, prompt):
    """Enhance a prompt using a Hugging Face model."""
    model = "facebook/bart-large-cnn"  # Example summarization/enhancement model
    return query_huggingface(api_key, model, f"Improve this prompt: {prompt}")
