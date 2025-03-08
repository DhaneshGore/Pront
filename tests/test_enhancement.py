# test_enhancement.py

import unittest
from enhancement import enhance_prompt

class TestEnhancement(unittest.TestCase):
    
    def setUp(self):
        self.api_key = "test_api_key"
        self.prompt = "Improve the clarity of this prompt."

    def test_enhance_with_gemini(self):
        """Test enhancing a prompt using Google Gemini."""
        result = enhance_prompt(self.api_key, "Google Gemini", self.prompt)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_enhance_with_huggingface(self):
        """Test enhancing a prompt using Hugging Face."""
        result = enhance_prompt(self.api_key, "Hugging Face Model", self.prompt)
        self.assertIsInstance(result, dict)  # Hugging Face API returns JSON
        self.assertIn("inputs", result)  # Expected key in response

if __name__ == "__main__":
    unittest.main()
