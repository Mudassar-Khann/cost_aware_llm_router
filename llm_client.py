import requests
from config import Settings
import os
from openai import OpenAI

settings = Settings()


class LLMClient:
    def __init__(self):
        self.api_key = settings.openrouter_api_key
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def send(self, payload):


        try:
            response = OpenAI.completions(
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
