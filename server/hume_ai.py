# https://github.com/HumeAI/hume-api-examples/blob/main/evi-python-example/run_evi.py

import asyncio
import os
import dotenv 
from hume import HumeVoiceClient, MicrophoneInterface, VoiceSocket

# Global variable to count messages
message_counter = 0

# Handler for when the connection is opened
def on_open():
    print("Say hello to EVI, Hume AI's Empathic Voice Interface!")

# Handler for incoming messages
def on_message(message):
    
    global message_counter
    
    # Increment the message counter for each received message
    message_counter += 1
    msg_type = message["type"]

    # Start the message box with the common header
    message_box = (
        f"\n{'='*60}\n"
        f"Message {message_counter}\n"
        f"{'-'*60}\n"
    )

    # Add role and content for user and assistant messages
    if msg_type in {"user_message", "assistant_message"}:
        
        role = message["message"]["role"]
        content = message["message"]["content"]
        
        message_box += (
            f"role: {role}\n"
            f"content: {content}\n"
            f"type: {msg_type}\n"
        )

        # Add top emotions if available
        if "models" in message and "prosody" in message["models"]:
            
            scores = message["models"]["prosody"]["scores"]
            num = 3
            
            # Get the top N emotions based on the scores
            top_emotions = get_top_n_emotions(prosody_inferences=scores, number=num)

            message_box += f"{'-'*60}\nTop {num} Emotions:\n"
            for emotion, score in top_emotions:
                message_box += f"{emotion}: {score:.4f}\n"

    # Add all key-value pairs for other message types, excluding audio_output
    elif msg_type != "audio_output":
        for key, value in message.items():
            message_box += f"{key}: {value}\n"
    else:
        message_box += (
            f"type: {msg_type}\n"
        )

    message_box += f"{'='*60}\n"
    
    # Print the constructed message box
    print(message_box)

# Function to get the top N emotions based on their scores
def get_top_n_emotions(prosody_inferences, number):
    sorted_inferences = sorted(prosody_inferences.items(), key=lambda item: item[1], reverse=True)
    return sorted_inferences[:number]

# Handler for when an error occurs
def on_error(error):
    print(f"Error: {error}")

# Handler for when the connection is closed
def on_close():
    print("Thank you for using EVI, Hume AI's Empathic Voice Interface!")

# Asynchronous handler for user input
async def user_input_handler(socket: VoiceSocket):
    while True:
        # Asynchronously get user input to prevent blocking other operations
        user_input = await asyncio.to_thread(input, "Type a message to send or 'Q' to quit: ")
        if user_input.strip().upper() == "Q":
            # If user wants to quit, close the connection
            print("Closing the connection...")
            await socket.close()
            break
        else:
            # Send the user input as text to the socket
            await socket.send_text_input(user_input)

# Asynchronous main function to set up and run the client
async def main() -> None:
    
    try:

        # Retrieve any environment variables stored in the .env file
        dotenv.load_dotenv()
        HUME_API_KEY = os.getenv("HUME_API_KEY")
        HUME_SECRET_KEY = os.getenv("HUME_SECRET_KEY")

        # Connect and authenticate with Hume
        client = HumeVoiceClient(HUME_API_KEY, HUME_SECRET_KEY)

        client_connection = client.connect_with_handlers(
            on_open=on_open,       # Handler for when the connection is opened
            on_message=on_message, # Handler for when a message is received
            on_error=on_error,     # Handler for when an error occurs
            on_close=on_close,     # Handler for when the connection is closed
            enable_audio=True,     # Flag to enable audio playback (True by default)
        )

        # Start streaming EVI over your device's microphone and speakers simultaneously
        async with client_connection as socket:
            microphone_task = asyncio.create_task(MicrophoneInterface.start(socket))
            user_input_task = asyncio.create_task(user_input_handler(socket))
            await asyncio.gather(microphone_task, user_input_task)
    
    # Catch and print any exceptions that occur
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())