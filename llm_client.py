import requests
import os
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def send(self, payload):


        try:
            response = requests.post(
                self.url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json=payload,
                timeout=15
            )

            if not response.ok:
                return {
                    "success": False,
                    "data": None,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }

            return {
                "success": True,
                "data": response.json(),
                "error": None
            }

        except Exception as e:
            return {
                "success": False,
                "data": None,
                "error": str(e)
            }
