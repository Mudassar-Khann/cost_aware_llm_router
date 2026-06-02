from config import Settings
from openai import OpenAI
import openai
from errors import (RateLimitError, InvalidRequestError,
 NetworkError, TimeoutError, AuthenticationError, PermissionDeniedError, ModelNotFoundError, ProviderError)

settings = Settings()

class LLMClient:
    def __init__(self):

        self.provider_name = "OpenRouter"

        self.Client = OpenAI(
            api_key = settings.openrouter_api_key,
            base_url= "https://openrouter.ai/api/v1"
        )


    def send(self, payload):

        model = payload["model"]


        try:
            response = self.Client.chat.completions.create(
                model= model,
                messages= payload["messages"],
                temperature= payload["temperature"],

                timeout=15

            )

            return {
                "success": True,
                "data": response,
                "error": None
            }

        except openai.AuthenticationError as e:
            return {
                "success": False,
                "data": None,
                "error": AuthenticationError("Authentication failed", model= model, provider=self.provider_name, cause_of_error= str(e))
            }

        except openai.PermissionDeniedError as e:
            return {
                "success": False,
                "data": None,
                "error": PermissionDeniedError("Permission denied", model= model, provider=self.provider_name, cause_of_error= str(e))
            }

        except openai.BadRequestError as e:
            return {
                "success": False,
                "data": None,
                "error": InvalidRequestError("Invalid request", model= model, provider=self.provider_name, cause_of_error= str(e))
            }
        except openai.RateLimitError as e:
            return {
                "success": False,
                "data": None,
                "error": RateLimitError("Rate limit exceeded", model= model, provider=self.provider_name, cause_of_error= str(e))
            }
        except openai.InternalServerError as e:
            return {
                "success": False,
                "data": None,
                "error": ProviderError("Provider error", model= model, provider=self.provider_name, cause_of_error= str(e))
            }
        except openai.NotFoundError as e:
            return {
                "success": False,
                "data": None,
                "error": ModelNotFoundError("Requested model was not found", model= model, provider=self.provider_name, cause_of_error= str(e))
            }
        except openai.APITimeoutError as e:
            return {
                "success": False,
                "data": None,
                "error": TimeoutError("Request timed out", model= model, provider=self.provider_name, cause_of_error= str(e))
            }
        except openai.APIConnectionError as e:
            return {
                "success": False,
                "data": None,
                "error": NetworkError("Network connection failed", model= model, provider=self.provider_name, cause_of_error= str(e))
            }
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "error": ProviderError("Something went wrong", model= model, provider=self.provider_name, cause_of_error= str(e))
            }
