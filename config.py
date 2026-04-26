class Config:
    CHEAP_MODEL = "openai/gpt-oss-20b:free"
    EXPENSIVE_MODEL = "openai/gpt-oss-120b:free"

    SYSTEM_PROMPT = "You are a helpful assistant."

    TEMPERATURE = 0.5

    PRICING = {
        CHEAP_MODEL: {
            "input": 3,
            "output": 15
        },
        EXPENSIVE_MODEL: {
            "input": 5,
            "output": 25
        }
    }
