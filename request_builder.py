from config import Config

class RequestBuilder:
    def build(self, user_input, model, mode="text"):
       

        system_prompt = Config.SYSTEM_PROMPT

        if mode == "json":
            system_prompt += "\nAlways respond in JSON with keys: answer, confidence"

        return {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            "temperature": Config.TEMPERATURE
        }
