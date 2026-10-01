from app.audio.microphone import record_audio
from app.audio.speech_to_text import SpeechToText

def main():

    print("------------------------------")
    print("       ASSISTENTE IA - V1     ")
    print("------------------------------")

    audio_file = record_audio(
        filename="command.wav",
        duration=5
    )

    speech = SpeechToText(
          model_name="base"
    )

    text = speech.transcribe(
          audio_file
    )

    # print(f"Áudio salvo em: {audio_file}")
    print()
    print("Você disse:")
    print(f'👉 "{text}"')

if __name__ == "__main__":
        main()