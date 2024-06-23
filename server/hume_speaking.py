import os
import dotenv
import asyncio
import nest_asyncio

from hume import HumeVoiceClient, MicrophoneInterface
# from hume.models.config import SessionSettings
from pydub import AudioSegment, playback

def play_audio(audio_data) -> None:
    # Play the audio response
    audio_segment = AudioSegment(
        data=audio_data,
        sample_width=2,   # Sample width in bytes
        frame_rate=16000, # Frame rate
        channels=1        # Number of channels
    )
    playback.play(audio_segment)

async def process_message(message) -> None:
    # Process and play the audio response
    if 'audio' not in message:
        audio_data = bytes(message['audio'])
        play_audio(audio_data)
    else:
        print("Received message:", message)

async def main() -> None:
    
    # Apply nest_asyncio to handle the event loop in environments like Jupyter Notebook
    nest_asyncio.apply()

    # Load environment variables from .env file
    dotenv.load_dotenv()
    HUME_API_KEY = os.getenv("HUME_API_KEY")
    EVI_CONFIG_ID = os.getenv("EVI_CONFIG_ID")
    
    # Confirm that environment variables were properly loaded
    if not HUME_API_KEY:
        raise ValueError("No API key found. Please set the HUME_API_KEY environment variable.")
    if not EVI_CONFIG_ID:
        raise ValueError("No EVI config ID found. Please set the EVI_CONFIG_ID environment variable.")

    # Connect to Hume
    client = HumeVoiceClient(HUME_API_KEY)

    # Establish a connection with EVI using existing configuration
    async with client.connect(config_id=EVI_CONFIG_ID) as socket:
        # Start listening to the microphone
        await MicrophoneInterface.start(socket)
        # Listen and process responses
        async for message in socket:
            await process_message(message)

if __name__ == "__main__":
    asyncio.run(main())