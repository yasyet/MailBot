
# --//[ESSENTIAL IMPORTS]\\--
import os
from dotenv import load_dotenv

# --//[LIBRARY IMPORTS]\\--
import openai

# --//[AI CLASS]\\--
class AIAgent:
    def __init__(self, _model: str, _temperature: float = 1.2, _max_tokens: int = 80):
        # --//|SETUP OPENAI CLIENT|--\\--
        self.client = openai.Client()
        self.model = _model
        self.temperature = _temperature
        self.max_tokens = _max_tokens

        # --//|LOAD DOTENV ENVIRONMENT VARIABLES|--\\--
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")

    def chat(self, messages: list[dict]) -> str:
        """
        Sends a chat message to the OpenAI API and returns the response.
        
        :param messages: List of messages to send to the AI.
        :return: The AI's response as a string.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                messages=messages
            )
            return response.choices[0].message['content']
        except Exception as e:
            return f"Error: {str(e)}"