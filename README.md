# Audio LLM Voice Assistant

The LLM Voice Assistant is a Python script that integrates voice recording, transcription, chat interaction with a language model that uses Llama-3-70b, and text-to-speech synthesis to create an interactive voice assistant experience.

## Features

- **Voice Recording**: Record audio through your microphone.
- **Transcription**: Convert recorded audio to text using AssemblyAI.
- **Chat Interaction**: Generate responses using Groq's language model.
- **Text-to-Speech**: Convert text responses to speech using ElevenLabs and play them back.
- **Interactive Loop**: Continuously interact with the assistant until you decide to quit.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.7+
- `pip` for installing required packages
- API keys for Groq, ElevenLabs, and AssemblyAI

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/sstechdev/audio-llm.git
    cd audio-llm
    ```

2. **Create a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the root directory of your project and add your API keys:

    ```ini
    GROQ_API_KEY=your_groq_api_key
    ELEVENLABS_API_KEY=your_elevenlabs_api_key
    ```

## Usage

1. **Run the script**:

    ```sh
    python script_name.py
    ```

2. **Interact with the assistant**:

    - Press Enter to start recording.
    - Speak into your microphone.
    - Wait for the transcription and response.
    - Listen to the generated audio response.
    - Repeat the process or type `q` to quit.

## Script Details

### Main Components

- **Environment Setup**: Loads API keys from the `.env` file.
- **Voice Recording**: Uses `pyaudio` to record audio input.
- **Transcription**: Sends audio to AssemblyAI for transcription.
- **Chat Interaction**: Sends transcribed text to Groq's language model and gets a response.
- **Text-to-Speech**: Converts the response text to speech using ElevenLabs.
- **Audio Playback**: Uses `pygame` to play back the generated audio.

### Key Functions

- `record_audio(filename, duration)`: Records audio and saves it to a file.
- `transcribe_audio(file_path)`: Transcribes the audio file to text using AssemblyAI.
- `chat_and_generate_audio(user_message)`: Gets a response from Groq and converts it to speech.
- `text_to_speech_file(text)`: Converts text to speech using ElevenLabs and returns the audio file path.
- `play_audio(audio_file_path)`: Plays the audio file using `pygame`.

### Error Handling

The script includes error handling for the following scenarios:

- API request failures.
- Transcription process failures.
- Timeout during transcription.

## Notes

- Ensure your microphone is properly set up and configured.
- The script continuously loops until you enter `q` when prompted.
- Adjust the `duration` parameter in the `record_audio` function if you need longer or shorter recordings.

## License

This project is licensed under the MIT License.

