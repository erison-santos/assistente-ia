import whisper

class SpeechToText:
    def __init__(self, model_name="base"):
        print("🧠 Carregando Whisper...")

        self.model = whisper.load_model(
            model_name,
            device="cpu"
        )

        print("✅ Whisper carregado.")
        
    def transcribe(self, audio_file: str) -> str:

        result = self.model.transcribe(
            audio_file,
            language="pt",
            fp16=False
        )

        return result["text"].strip()