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

    Models_Token_Pricing  = {

    "openai/gpt-oss-20b:free" : {
        "cost_per_1m_input" : 3,
        "cost_per_1m_output" : 15
    },
    "openai/gpt-oss-120b:free" : {
        "cost_per_1m_input" : 5,
        "cost_per_1m_output" : 25
    }


    }

    

