from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    openai_api_key: str = "API key missing"



class Config:

    env_file = ".env"



    system_promt ={
        "code" : "Act as expert Software Enginner give effcient code and tell why it works",
        "small" : "Give the concise and relevent answer to the qustion make sure not to add extra details",
        "detail"  :  "Explain like subject expert give analogies and real life explan to uderstand the topic better"
    }

    temprature = {
        "code" : 0.2,
        "small" : 0.3,
        "detail"  : 0.7
    }

    cost_of_models = {
        "cheap" :
    }


