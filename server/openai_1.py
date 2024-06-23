import os
import openai
from dotenv import load_dotenv

load_dotenv()
# Get the OpenAI API key from the environment variable
key = os.getenv("OPEN_API_KEY")
openai.api_key = (key)
chat_completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    # instructions="You are a job interview grader. You give feedback to the voice tone and emotions.",
    messages=[
        {"role": "user", "content": "output this is a test only"}
    ],
)
response_content = chat_completion.choices[0].message.content
print(response_content)