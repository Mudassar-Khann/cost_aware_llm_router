from config import Settings
from openai import OpenAI

settings = Settings()


class LLMClient:
    def __init__(self):

        self.Client = OpenAI(
            api_key = settings.openrouter_api_key,
            base_url= "https://openrouter.ai/api/v1"
        )


    def send(self, payload):

        try:
            response = self.Client.chat.completions.create(
                messages= payload,
                timeout=15

            )

            return {
                "success": True,
                "data": response,
                "error": None
            }

        except Exception as e:
            return {
                "success": False,
                "data": None,
                "error": str(e)
            }
