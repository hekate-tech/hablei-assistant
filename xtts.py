from TTS.api import TTS

print("Carregando XTTS...")

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    gpu=False

)


def generate_speech(
        text: str,
        speaker: str,
        output_path: str):

    tts.tts_to_file(
        text=text,
        speaker_wav=speaker,
        language="pt",
        file_path=output_path
    )