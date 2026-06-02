class LLMError(Exception):
    def __init__(
            self,
            message: str,
            provider: str = None,
            model: str = None,
            raw_response: str = None
            ):

        super().__init__(message)
        self.provider = provider
        self.model = model
        self.raw_response = raw_response


class AuthenticationError(LLMError):
    pass


class RateLimitError(LLMError):
    pass


class InvalidRequestError(LLMError):
    pass


class ModelNotFoundError(LLMError):
    pass


class ProviderError(LLMError):
    pass

class TimeoutError(LLMError):
    pass

class NetworkError(LLMError):
    pass
