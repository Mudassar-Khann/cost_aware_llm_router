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

        metadata = {
            "success": False,
            "data": None,
            "error": None
            }


        try:
            response = self.Client.chat.completions.create(
                model= model,
                messages= payload["messages"],
                temperature= payload["temperature"],

                timeout=15

            )

            metadata["success"] = True
            metadata["data"] = response

            return metadata



        except openai.AuthenticationError as e:

                   metadata["error"] = AuthenticationError("Authentication failed", model= model, provider=self.provider_name, cause_of_error= str(e))


        except openai.PermissionDeniedError as e:

                   metadata["error"] = PermissionDeniedError("Permission denied", model= model, provider=self.provider_name, cause_of_error= str(e))


        except openai.BadRequestError as e:

                   metadata["error"] = InvalidRequestError("Invalid request", model= model, provider=self.provider_name, cause_of_error= str(e))

        except openai.RateLimitError as e:

                   metadata["error"] = RateLimitError("Rate limit exceeded", model= model, provider=self.provider_name, cause_of_error= str(e))

        except openai.InternalServerError as e:

                   metadata["error"] = ProviderError("Provider error", model= model, provider=self.provider_name, cause_of_error= str(e))

        except openai.NotFoundError as e:

                   metadata["error"] = ModelNotFoundError("Requested model was not found", model= model, provider=self.provider_name, cause_of_error= str(e))

        except openai.APITimeoutError as e:

                   metadata["error"] = TimeoutError("Request timed out", model= model, provider=self.provider_name, cause_of_error= str(e))

        except openai.APIConnectionError as e:

                   metadata["error"] = NetworkError("Network connection failed", model= model, provider=self.provider_name, cause_of_error= str(e))

        except Exception as e:

                  metadata["error"] = ProviderError("Something went wrong", model= model, provider=self.provider_name, cause_of_error= str(e))

        return metadata

