from config import Config
class ModelSelection:

    def __init__(self):

        self.model = {
            "small" : {
                "model": "openai/gpt-oss-20b:free",
                "messeges" : [
                    {
                        "role" : "system",
                        "content" : Config.system_promt.get("concise")
                    },
                    {
                        "role" : "user",
                        "content" : self.message
                    }

                ],
                "temprature" : Config.temprature.get("concise", 0.7)
            },

            "code" : {
                "model" : "openai/gpt-oss-120b:free",
                "messeges" : [
                    {
                        "role" : "system",
                        "content" : Config.system_promt.get("very_concise")
                    },
                    {
                        "role" : "user",
                        "content" :  self.message
                    }

                ],
                "temprature" : Config.temprature.get("very_concise", 0.2)


            },

            "detail" : {

                "model" : "openai/gpt-oss-120b:free",
                "messeges" : [
                    {
                        "role" : "system",
                        "content" : Config.system_promt.get("detail", "Elaborate")
                    },
                    {
                        "role" : "user",
                        "content" : self.message
                    }

                ],
                "temprature" : Config.temprature.get("detail", 0.7)

            }

        }

        self.detaling = {"detail", "elaborate", "explain", "examples" }
        self.coding = {"cpp", "c++", "python", "code", "coding", "java" }



    def selct_model(self, message):
            if not message:
                return None
            if message.lower().split() in list(self.detaling):
                return self.model["detail"]
            if message.lower().split() in list(self.coding):
                return self.model["code"]

            else:
                return self.model["small"]











