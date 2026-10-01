import os

from dotenv import load_dotenv
from openai import OpenAI
from app.ai.provider import AIProvider

load_dotenv()

class OpenAIProvider(AIProvider):
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError("OPENAI_API_KEY não foi encontrada no arquivo .env")

        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text