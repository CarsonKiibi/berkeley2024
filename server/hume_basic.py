import os
import dotenv
import asyncio

from hume import HumeVoiceClient, MicrophoneInterface

async def main() -> None:
    
    # Get data from .env file
    dotenv.load_dotenv()
    HUME_API_KEY = os.getenv("HUME_API_KEY")
    EVI_CONFIG_ID = os.getenv("EVI_CONFIG_ID")

    # Connect to Hume
    client = HumeVoiceClient(HUME_API_KEY)

    # Establish a connection with EVI using existing configuration
    async with client.connect(config_id=EVI_CONFIG_ID) as socket:
        # Start listening to the microphone
        await MicrophoneInterface.start(socket)
                
if __name__ == "__main__":
    asyncio.run(main())