# gemini_api.py

import google.generativeai as genai

def configure_gemini(api_key):
    """Configure the Google Gemini API with the provided API key."""
    genai.configure(api_key=api_key)

def query_gemini(api_key, prompt):
    """Query the Google Gemini API for text generation or enhancement."""
    configure_gemini(api_key)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

def analyze_prompt_gemini(api_key, prompt):
    """Analyze a prompt using Google Gemini."""
    return query_gemini(api_key, f"Analyze this prompt for clarity and completeness: {prompt}")

def enhance_prompt_gemini(api_key, prompt):
    """Enhance a prompt using Google Gemini."""
    return query_gemini(api_key, f"Improve this prompt: {prompt}")
