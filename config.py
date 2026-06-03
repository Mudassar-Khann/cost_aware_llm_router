from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openrouter_api_key: str

    model_config = SettingsConfigDict(env_file=".env")

class Config:

    SYSTEM_PROMPT = "You are a helpful assistant."

    TEMPERATURE = 0.5

    MAX_RETRIES = 3

    DEFAULT_MODEL = "gpt_oss_20b"

    EFFCIENT_MODEL = "gpt_oss_120b"


MODELS = {
    "gpt_oss_20b": {
        "name": "GPT OSS 20B",

        "api_name": "openai/gpt-oss-20b:free",

        "provider": "openrouter",
        "developer": "openai",

        "available": True,

        "pricing": {
            "input_per_million": 3,
            "output_per_million": 15
        }
    },

    "gpt_oss_120b": {
        "name": "GPT OSS 120B",

        "api_name": "openai/gpt-oss-120b:free",

        "provider": "openrouter",
        "developer": "openai",

        "available": True,

        "pricing": {
            "input_per_million": 5,
            "output_per_million": 25
        }
    }
}
