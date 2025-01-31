# test_analysis.py

import unittest
from analysis import analyze_prompt

class TestAnalysis(unittest.TestCase):
    
    def setUp(self):
        self.api_key = "test_api_key"
        self.prompt = "Analyze the impact of AI on education."

    def test_analyze_with_gemini(self):
        """Test analyzing a prompt using Google Gemini."""
        result = analyze_prompt(self.api_key, "Google Gemini", self.prompt)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_analyze_with_huggingface(self):
        """Test analyzing a prompt using Hugging Face."""
        result = analyze_prompt(self.api_key, "Hugging Face Model", self.prompt)
        self.assertIsInstance(result, dict)  # Hugging Face API returns JSON
        self.assertIn("inputs", result)  # Expected key in response

if __name__ == "__main__":
    unittest.main()
