from dotenv import load_dotenv
import os
import requests

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {openai_key}",
    "Content-Type": "application/json",
  },
  json={
    "model": "openai/gpt-oss-120b:free",
    "messages": [
        {
          "role": "user",
          "content": "How many r's are in the word 'strawberry'?"
        }
      ],


  }
)

# Extract the assistant message with reasoning_details
response = response.json()
response = response['choices'][0]['message']["content"]

print(response)


