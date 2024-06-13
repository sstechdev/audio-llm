import os
from dotenv import load_dotenv
import tempfile
from groq import Groq
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import pygame
import shutil
import uuid

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
eleven_labs_client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

pygame.mixer.init()

# create folder 
audio_folder = "Jarvis-voice-0.1"
os.makedirs(audio_folder, exist_ok=True)

def chat_and_generate_audio(user_message):
    # get qroq API response
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-8b-8192",
    )
    response_text = chat_completion.choices[0].message.content
    print(f"LLM Response: {response_text}")

    # convert chat to audio 
    temp_file_path = text_to_speech_file(response_text)

    output_file = os.path.join(audio_folder, f"llm-voice-response-{uuid.uuid4().hex}.mp3")

    # move temporary file to the desired output file
    shutil.move(temp_file_path, output_file)

    play_audio(output_file)

def text_to_speech_file(text: str) -> str:
    response = eleven_labs_client.text_to_speech.convert(
        voice_id="29vD33N1CtxCmqQRPOHJ",  
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",  
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        for chunk in response:
            if chunk:
                temp_file.write(chunk)
        temp_file_path = temp_file.name

    print(f"{temp_file_path}: A new temporary audio file was created successfully!")


    return temp_file_path

def play_audio(audio_file_path):
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# user input loop
while True:
    user_input = input("Enter your message (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    chat_and_generate_audio(user_input)


pygame.mixer.quit()
