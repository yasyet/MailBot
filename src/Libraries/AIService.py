# --//[ESSENTIAL IMPORTS]\\--
import os
from dotenv import load_dotenv
import google.generativeai as genai


# --//[AI CLASS]\\--
class AIAgent:
    def __init__(self, model: str = "gemini-2.5-flash-lite", temperature: float = 1.0, max_output_tokens: int = 80):
        """
        Initialize Gemini AI client.
        
        :param model: Gemini model name
        :param temperature: Controls randomness
        :param max_output_tokens: Max tokens in response
        """
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")

        genai.configure(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_output_tokens = max_output_tokens

    def chat(self, prompt: str) -> str:
        """
        Sends a single prompt to Gemini API and returns response text.
        
        :param prompt: The user input string.
        :return: AI response as text.
        """
        try:
            model_instance = genai.GenerativeModel(self.model)
            response = model_instance.generate_content(
                contents=prompt,
                generation_config={
                    "temperature": self.temperature,
                    "max_output_tokens": self.max_output_tokens
                }
            )
            return response.text.strip()
        except Exception as e:
            return f"Error: {str(e)}"


# --//[EXAMPLE USAGE]\\--
if __name__ == "__main__":
    agent = AIAgent()
    print(agent.chat("Write a short poem about the ocean."))
