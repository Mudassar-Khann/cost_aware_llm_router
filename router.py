from config import Config
class ModelSelection:

    def __init__(self):
        self.Expensive_Model = {"detail", "elaborate", "explain", "examples", "story", "why", "how", "compare", "design"}
        self.Coding_Model = {"cpp", "c++", "python", "code", "coding", "java"}

    def build_model(self, model_type, content, mode):
        with open("docs.txt", "r", encoding="utf-8") as f:
           Docs = f.read()

        return {
            "model": {
                "small": "openai/gpt-oss-20b:free",
                "code": "openai/gpt-oss-120b:free",
                "detail": "openai/gpt-oss-120b:free"
            }[model_type],

            "messages": [
                {
                    "role": "system",
                    "contnet" : {

                              "text" : "Provide structured text reasponse. Avoide conjuction give gaps and highlits for importnat points",
                              "json" : "Always respond in JSON with keys: answer, confidence",
                              "code" : "Provide effcinet code chunks if asked for full provide large snippets"
                                 }[mode]
                },
                {
                    "role": "system",
                    "content": Config.system_promt.get(model_type, "Default")
                },
                {
                    "role": "user",
                    "content" : Docs
                },
                {
                    "role": "user",
                    "content": content
                }


            ],

            "temperature": Config.temprature.get(model_type, 0.7)
        }

    def select_model(self, message, mode = "text"):
        if not message:
            return None

        words = set(message.lower().split())

        if "why" in words and len(words) <= 6:
            return self.build_model("small", message, mode)

        if words & self.Expensive_Model or len(words) >= 20:
            return self.build_model("detail", message, mode)

        if words & self.Coding_Model:
            return self.build_model("code", message, mode)

        return self.build_model("small", message, mode)
