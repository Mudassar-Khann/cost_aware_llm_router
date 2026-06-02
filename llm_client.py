from config import Settings
from openai import OpenAI
from errors import (LLMError, RateLimitError, InvalidRequestError,
 NetworkError, TimeOutError, AuthenticationError, ModelNotFoundError, ProviderError)

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
                model= payload["model"],
                messages= payload["messages"],
                temperature= payload["temperature"],

                timeout=15

            )

            return {
                "success": True,
                "data": response,
                "error": None
            }

        except AuthenticationError:
            return {
                "success": False,
                "data": None,
                "error": AuthenticationError("Write APi key correctly")
            }

        except InvalidRequestError:
            return {
                "success": False,
                "data": None,
                "error": InvalidRequestError("Invalid Request")
            }
        except RateLimitError:
            return {
                "success": False,
                "data": None,
                "error": RateLimitError("Token Limit Exceeded")
            }
        except ProviderError:
            return {
                "success": False,
                "data": None,
                "error": ProviderError("Server Side error")
            }
        except ModelNotFoundError:
            return {
                "success": False,
                "data": None,
                "error": ModelNotFoundError("This model dosn't exist")
            }
        except TimeOutError:
            return {
                "success": False,
                "data": None,
                "error": TimeOutError("Given Time Exceded")
            }
        except NetworkError:
            return {
                "success": False,
                "data": None,
                "error": NetworkError("Network Busy")
            }
        except LLMError:
            return {
                "success": False,
                "data": None,
                "error": LLMError
            }
