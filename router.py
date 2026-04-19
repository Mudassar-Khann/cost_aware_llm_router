class ModelSelection:

    def __init__(self):
        self.detaling = {"detail", "elaborate", "explain", "examples"}
        self.coding = {"cpp", "c++", "python", "code", "coding", "java"}

    def build_model(self, model_type, content):
        return {
            "model": {
                "small": "openai/gpt-oss-20b:free",
                "code": "openai/gpt-oss-120b:free",
                "detail": "openai/gpt-oss-120b:free"
            }[model_type],

            "messages": [
                {
                    "role": "system",
                    "content": Config.system_promt.get(model_type, "Default")
                },
                {
                    "role": "user",
                    "content": content   # ✅ always fresh
                }
            ],

            "temperature": Config.temprature.get(model_type, 0.7)
        }

    def select_model(self, message):
        if not message:
            return None

        words = set(message.lower().split())

        if words & self.detaling:
            return self.build_model("detail", message)

        if words & self.coding:
            return self.build_model("code", message)

        return self.build_model("small", message)
