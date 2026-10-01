import json
from pydantic import BaseModel

SYSTEM_PROMPT = """
Você é o interpretador de comandos de um assistente pessoal para Windows.

Sua função NÂO é executar comandos.

Sua função é interpretar o que o usuário deseja fazer e retornar uma inteção estruturada.

Possíveis inteções:
- open_application
- open_website
- open_folder
- system_command
- search_web
- unknown

Retorne SOMENTE JSON válido.

Exemplo:

{
    
    "intent": "open_application",
    "target": "chrome",
    "parameters": {},
    "confidence": 0.98
}

Se não tiver certeza:

{
    "intent": "unknown",
    "target": "null",
    "parameters": {},
    "confidence": 0.30
}
"""

class Intent(BaseModel):
    intent: str
    target: str | None = None
    parameters: dict = {}
    confidence: float = 0.0

def build_prompt(user_text: str) -> str:

    return f"""
{SYSTEM_PROMPT}

Comando do usuário: "{user_text}"
"""

def parse_intent(response: str) -> Intent:
    try:
        data = json.loads(response)
        return Intent(**data)
    except json.JSONDecodeError:
        return Intent(
            intent="unknown",
            target=None,
            parameters={},
            confidence=0.0
        )