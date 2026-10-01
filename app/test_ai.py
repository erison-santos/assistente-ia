#from app.ai.openai_provider import OpenAIProvider
#from app.ai.groq_provider import GroqProvider
from app.ai.factory import crate_ai_provider
from app.core.intent import build_prompt, parse_intent

def main():

    provider = crate_ai_provider()
    
    user_text = "Abra o Google Chrome"

    prompt = build_prompt(user_text)

    response = provider.generate(prompt)

    print()
    print("Resposta da IA:")
    print(response)

    intent = parse_intent(response)

    print()
    print("Intenção interpretada:")
    print(intent.model_dump())

if __name__ == "__main__":
    main()