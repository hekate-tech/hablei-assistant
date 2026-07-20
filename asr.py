from faster_whisper import WhisperModel

print("Carregando Faster-Whisper...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def transcribe(audio_path: str) -> str:
    """
    transcribes an audio file to text.
    
    """

    segments, info = model.transcribe(audio_path)

    transcription = ""

    for segment in segments:
        transcription += segment.text + " "

    return transcription.strip()