import google.generativeai as genai
import requests
from config.settings import CONFIG

def enhance_with_gemini(api_key, prompt):
    """Enhance prompt using Google Gemini API."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Improve this prompt: {prompt}")
    
    # Ensure enhancement includes time complexity analysis and edge cases
    enhanced_text = response.text
    if "time complexity analysis" not in enhanced_text.lower():
        enhanced_text += "\nInclude time complexity analysis and handle edge cases like empty arrays."
    
    return enhanced_text

def enhance_with_huggingface(api_key, prompt):
    """Enhance prompt using Hugging Face API."""
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(CONFIG["HUGGINGFACE_API_URL"], headers=headers, json={"inputs": f"Improve this prompt: {prompt}"})
    
    enhanced_text = response.json() if response.status_code == 200 else "Error: Unable to process request."
    if isinstance(enhanced_text, dict) and "generated_text" in enhanced_text:
        enhanced_text = enhanced_text["generated_text"]
    
    # Ensure enhancement includes time complexity analysis and edge cases
    if "time complexity analysis" not in enhanced_text.lower():
        enhanced_text += "\nInclude time complexity analysis and handle edge cases like empty arrays."
    
    return enhanced_text

def enhance_prompt(api_key, model_choice, prompt):
    """Select and use the appropriate LLM for prompt enhancement."""
    if model_choice == "Google Gemini":
        return enhance_with_gemini(api_key, prompt)
    else:
        return enhance_with_huggingface(api_key, prompt)
