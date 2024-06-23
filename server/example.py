import os
from hume import HumeVoiceClient, MicrophoneInterface
from dotenv import load_dotenv
import asyncio

async def main() -> None:
    
    load_dotenv()
    HUME_API_KEY = os.getenv("HUME_API_KEY")
    EVI_CONFIG_ID = os.getenv("EVI_CONFIG_ID")

    client = HumeVoiceClient(HUME_API_KEY)

    # Establish a connection with EVI with your configuration by passing
    # the config_id as an argument to the connect method
    async with client.connect(config_id=EVI_CONFIG_ID) as socket:
        await MicrophoneInterface.start(socket)


# Run the main function
asyncio.run(main())
