import sounddevice as sd
import soundfile as sf


SAMPLE_RATE = 16000
CHANNELS = 1


def record_audio(
    filename: str = "command.wav",
    duration: int = 5,
) -> str:

    print()
    print("🎙️ Gravando...")
    print("Fale agora!")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32",
    )

    sd.wait()

    sf.write(
        filename,
        audio,
        SAMPLE_RATE,
    )

    print("✅ Gravação concluída.")

    return filename