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

        except openai.AuthenticationError:
            return {
                "success": False,
                "data": None,
                "error": AuthenticationError("Write APi key correctly", model= model, provider=self.provider_name)
            }

        except openai.PermissionDeniedError:
            return {
                "success": False,
                "data": None,
                "error": PermissionDeniedError("You Do Not have the permission to acess this material", model= model, provider=self.provider_name)
            }

        except openai.BadRequestError:
            return {
                "success": False,
                "data": None,
                "error": InvalidRequestError("Invalid Request", model= model, provider=self.provider_name)
            }
        except openai.RateLimitError:
            return {
                "success": False,
                "data": None,
                "error": RateLimitError("Token Limit Exceeded", model= model, provider=self.provider_name)
            }
        except openai.InternalServerError:
            return {
                "success": False,
                "data": None,
                "error": ProviderError("Server Side error", model= model, provider=self.provider_name)
            }
        except openai.NotFoundError:
            return {
                "success": False,
                "data": None,
                "error": ModelNotFoundError("This model dosn't exist", model= model, provider=self.provider_name)
            }
        except openai.APITimeoutError:
            return {
                "success": False,
                "data": None,
                "error": TimeoutError("Given Time Exceded", model= model, provider=self.provider_name)
            }
        except openai.APIConnectionError:
            return {
                "success": False,
                "data": None,
                "error": NetworkError("Network Busy", model= model, provider=self.provider_name)
            }
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "error": ProviderError("Something went wrong", model= model, provider=self.provider_name, raw_response= str(e))
            }
