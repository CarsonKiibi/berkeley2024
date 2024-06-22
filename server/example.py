import os
from hume import HumeVoiceClient, MicrophoneInterface
from dotenv import load_dotenv
import asyncio

async def main() -> None:
    
    load_dotenv()
    CHARLIE_HUME_API_KEY = os.getenv("CHARLIE_HUME_API_KEY")
    client = HumeVoiceClient(CHARLIE_HUME_API_KEY)

    # Start streaming EVI over your device's microphone and speakers 
    async with client.connect() as socket:
        await MicrophoneInterface.start(socket)

asyncio.run(main())