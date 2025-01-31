def select_llm(prompt):
    """Select the best LLM based on prompt complexity and type."""
    
    # Heuristic-based selection
    if "code" in prompt.lower() or "function" in prompt.lower():
        return "Google Gemini"  # Better for code generation
    else:
        return "Hugging Face Model"  # Better for general NLP tasks
