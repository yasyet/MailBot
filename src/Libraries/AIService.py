
# --//[ESSENTIAL IMPORTS]\\--
import os
from dotenv import load_dotenv

# --//[LIBRARY IMPORTS]\\--
import openai

# --//[AI CLASS]\\--
class AIAgent:
    def __init__(self: str):
        # --//|SETUP OPENAI CLIENT|--\\--
        self.client = openai.Client()

        # --//|LOAD DOTENV ENVIRONMENT VARIABLES|--\\--
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")

    def chat(self, messages: list[dict], model: str) -> str:
        """
        Sends a chat message to the OpenAI API and returns the response.
        
        :param messages: List of messages to send to the AI.
        :return: The AI's response as a string.
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=1.2,
                max_tokens=80
            )
            return response.choices[0].message['content']
        except Exception as e:
            return f"Error: {str(e)}"