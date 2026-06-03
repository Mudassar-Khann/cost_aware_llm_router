from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openrouter_api_key: str

    model_config = SettingsConfigDict(env_file=".env")

class Config:

    SYSTEM_PROMPT = "You are a helpful assistant."

    TEMPERATURE = 0.5

    MAX_RETRIES = 3


    AVAILABLE_MODELS = {
    "gpt_oss_20b": {
        "api_name": "openai/gpt-oss-20b:free",
        "display_name": "GPT OSS 20B",
        "provider": "OpenRouter",
        "company": "OpenAI",
        "available": True,
        "pricing": {
            "input": 3,
            "output": 15
        }
    },

    "gpt_oss_120b": {
        "api_name": "openai/gpt-oss-120b:free",
        "display_name": "GPT OSS 120B",
        "provider": "OpenRouter",
        "company": "OpenAI",
        "available": True,
        "pricing": {
            "input": 5,
            "output": 25
        }
    }
}
