import os
from hume import HumeVoiceClient, MicrophoneInterface
from dotenv import load_dotenv
import asyncio

async def main() -> None:
    
    load_dotenv()
    HUME_API_KEY = os.getenv("HUME_API_KEY")
    EVI_CONFIG_ID = os.getenv("EVI_CONFIG_ID")

    client = HumeVoiceClient(HUME_API_KEY)

    # Established a connection with EVI with your configuration by passing
    # the config_id as an argument to the connect method
    async with client.connect(config_id=EVI_CONFIG_ID) as socket:
        await MicrophoneInterface.start(socket)


#######
    # # Connect and authenticate with Hume
    # client = HumeVoiceClient(HUME_API_KEY)

    # # Establish a connection with EVI using the predefined configuration in the playground
    # async with client.connect(config_id=EVI_CONFIG_ID) as socket:
    #     # Start streaming audio from the microphone
    #     async with MicrophoneInterface.start(socket):
    #         # Listen and process responses
    #         async for message in socket:
    #             await process_message(message)
#######

# Run the main function
asyncio.run(main())





# #######
# import nest_asyncio

# import os
# import asyncio
# import nest_asyncio
# from dotenv import load_dotenv
# from hume import HumeVoiceClient, MicrophoneInterface
# # from hume.models.config import SessionSettings
# from pydub import AudioSegment
# from pydub.playback import play

# # Apply nest_asyncio to handle the event loop in environments like Jupyter Notebook
# nest_asyncio.apply()

# # Function to play the audio response
# def play_audio(audio_data):
#     audio_segment = AudioSegment(
#         data=audio_data,
#         sample_width=2,  # Sample width in bytes
#         frame_rate=16000,  # Frame rate
#         channels=1  # Number of channels
#     )
#     play(audio_segment)

# async def process_message(message):
#     # Process and play the audio response
#     if 'audio' in message:
#         audio_data = bytes(message['audio'])
#         play_audio(audio_data)
#     else:
#         print("Received message:", message)

# async def main() -> None:
#     # Load environment variables from .env file
#     load_dotenv()
#     HUME_API_KEY = os.getenv("HUME_API_KEY")
#     EVI_CONFIG_ID = os.getenv("EVI_CONFIG_ID")
    
#     if not HUME_API_KEY:
#         raise ValueError("No API key found. Please set the HUME_API_KEY environment variable.")
#     if not EVI_CONFIG_ID:
#         raise ValueError("No EVI config ID found. Please set the EVI_CONFIG_ID environment variable.")

#     # Connect and authenticate with Hume
#     client = HumeVoiceClient(HUME_API_KEY)

#     # Establish a connection with EVI using the predefined configuration in the playground
#     async with client.connect(config_id=EVI_CONFIG_ID) as socket:
#         # Start streaming audio from the microphone
#         await MicrophoneInterface.start(socket)
        
#         # Listen and process responses
#         async for message in socket:
#             await process_message(message)

# # Run the main function
# asyncio.run(main())

# #######