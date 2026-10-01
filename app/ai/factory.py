import os

from dotenv import load_dotenv
from app.ai.provider import AIProvider
from app.ai.groq_provider import GroqProvider

load_dotenv()

def crate_ai_provider() -> AIProvider:
    
    provider_name = os.getenv(
        "AI_PROVIDER",
        "groq"
    ).lower()

    if provider_name == "groq":
        return GroqProvider()

    raise ValueError(f"Provedor de IA não suportado: {provider_name}")