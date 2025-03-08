import google.generativeai as genai
import requests
from config.settings import CONFIG

def analyze_with_gemini(api_key, prompt):
    """Analyze prompt using Google Gemini API."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

def analyze_with_huggingface(api_key, prompt):
    """Analyze prompt using Hugging Face API."""
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(CONFIG["HUGGINGFACE_API_URL"], headers=headers, json={"inputs": prompt})
    return response.json() if response.status_code == 200 else "Error: Unable to process request."

def analyze_prompt(api_key, model_choice, prompt):
    """Select and use the appropriate LLM for prompt analysis."""
    if model_choice == "Google Gemini":
        return analyze_with_gemini(api_key, prompt)
    else:
        return analyze_with_huggingface(api_key, prompt)
