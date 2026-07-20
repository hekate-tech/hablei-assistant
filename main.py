import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from asr import transcribe
from llm import generate_response
from xtts import generate_speech
from utils import run_with_progress


INPUT_AUDIO = "audios/macarrao-privada.wav"
VOICE = "audios/macarrao-privada.wav"
# VOICE = "audios/clonar-larissa.wav"

OUTPUT_FOLDER = "output"

TRANSCRIPTION_FILE = os.path.join(OUTPUT_FOLDER, "transcription.txt")
RESPONSE_FILE = os.path.join(OUTPUT_FOLDER, "response.txt")
AUDIO_RESPONSE = os.path.join(OUTPUT_FOLDER, "response.wav")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


print("=" * 60)
print("HEKATE VOICE ASSISTANT")
print("=" * 60)


# Speech-to-Text

text = run_with_progress(
    transcribe,
    "Transcribing audio",
    INPUT_AUDIO
)

print("\nTranscription:")
print(text)

with open(TRANSCRIPTION_FILE, "w", encoding="utf-8") as f:
    f.write(text)


# LLM

response = run_with_progress(
    generate_response,
    "Generating response",
    text
)

print("\nResponse:")
print(response)

with open(RESPONSE_FILE, "w", encoding="utf-8") as f:
    f.write(response)


# Text-to-Speech

run_with_progress(
    generate_speech,
    "Synthesizing speech",
    response,
    VOICE,
    AUDIO_RESPONSE
)


print("\n" + "=" * 60)
print("Execution completed.")
print("=" * 60)

print(f"Transcription : {TRANSCRIPTION_FILE}")
print(f"Response      : {RESPONSE_FILE}")
print(f"Audio         : {AUDIO_RESPONSE}")