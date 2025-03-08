# 📝 Prompt Analysis & Enhancement System

## 📌 Project Overview
This project provides an **advanced system for analyzing and enhancing prompts** using **Google Gemini API** and **Hugging Face API**. It helps improve prompt clarity, completeness, and specificity while selecting the best LLM for the task.

## 🚀 Features
- **Prompt Analysis:** Identifies missing elements, clarity score, and context completeness.
- **LLM Selection:** Recommends either **Google Gemini** or **Hugging Face** based on prompt complexity.
- **Prompt Enhancement:** Improves the given prompt using **prompt engineering techniques**.
- **Structured JSON Output:** Generates an output with enhanced prompts and improvement metrics.
- **Streamlit UI:** User-friendly interface for easy input and results display.

## 📂 Project Structure
```
📂 Prompt-Enhancer/
│── 📄 app.py                      # Streamlit app (Main entry point)
│── 📂 config/                     # Configuration files
│   ├── 📄 __init__.py              # Marks the directory as a package
│   ├── 📄 settings.py              # Configuration settings
│── 📂 utils/                       # Utility functions
│   ├── 📄 __init__.py              # Marks the directory as a package
│   ├── 📄 analysis.py              # Prompt analysis functions
│   ├── 📄 enhancement.py           # Prompt enhancement functions
│   ├── 📄 llm_selection.py         # LLM selection logic
│── 📂 models/                      # LLM API integrations
│   ├── 📄 __init__.py              # Marks the directory as a package
│   ├── 📄 gemini_api.py            # Google Gemini API wrapper
│   ├── 📄 huggingface_api.py       # Hugging Face API wrapper
│── 📂 tests/                       # Unit tests
│   ├── 📄 __init__.py              # Marks the directory as a package
│   ├── 📄 test_analysis.py         # Tests for analysis module
│   ├── 📄 test_enhancement.py      # Tests for enhancement module
│── 📂 venv/                        # Virtual environment (ignore in Git)
│── 📄 requirements.txt             # Python dependencies
│── 📄 README.md                    # Project documentation
│── 📄 .gitignore                   # Ignore unnecessary files
```

## 🔧 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DhaneshGore/Prompt-Analysis-Enhancement-System.git
cd Prompt-Enhancer
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
```bash
conda create --name prompt_env python=3.9
conda activate prompt_env
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Streamlit App
Start the Streamlit web application:
```bash
streamlit run app.py
```
This will open the app in your **browser**.

## 🧪 Running Tests
Run unit tests to verify that everything is working correctly:
```bash
python -m unittest discover tests
```

## 📜 Example Input/Output
### **Example Input:**
```json
{
    "prompt": "write code for sorting array"
}
```

### **Expected Output:**
```json
{
    "analysis": {
        "missing_elements": ["array type", "sorting order", "performance requirements"],
        "context_score": 0.4,
        "clarity_score": 0.5
    },
    "recommended_llm": {
        "model": "Google Gemini",
        "reasoning": "Technical task requiring code generation and understanding of implementation details"
    },
    "enhanced_prompt": {
        "text": "Write a Python function to sort an array of integers in ascending order. Include time complexity analysis and handle edge cases like empty arrays.",
        "technique": "Specification Expansion",
        "improvement_metrics": {
            "clarity": +0.4,
            "context": +0.5,
            "specificity": +0.6
        }
    }
}
```

## 🚀 Deploying with Docker
### 1️⃣ Build the Docker Image
```bash
docker build -t your-dockerhub-username/prompt-analyzer .
```

### 2️⃣ Run the Docker Container Locally
```bash
docker run -p 8501:8501 your-dockerhub-username/prompt-analyzer
```

### 3️⃣ Push the Image to Docker Hub
```bash
docker login
docker push your-dockerhub-username/prompt-analyzer
```

## 🛠️ Future Enhancements
- Add support for more LLMs like **Anthropic Claude** and **Cohere**.
- Implement **logging & error handling** for improved debugging.
- Allow **fine-tuning** prompts dynamically based on user feedback.

## 📌 License
This project is licensed under the MIT License.

---

**🚀 Happy Prompt Engineering!** 🎯
