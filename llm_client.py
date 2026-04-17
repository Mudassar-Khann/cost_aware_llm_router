from dotenv import load_dotenv
import os
import requests





errors = {
    400 : "Api request is invalid somthing is missing fix your input",
    401 : "unauthorized tookes missing or wrong api",
    404 : "Model you requsted dosn't exist ",
    429 : "limit exceeded",
    500 : "sever error"
}


def send_response(data: dict, errors = errors):

    if not data:
        return "can't give answer to empty message"

    load_dotenv()
    openai_api = os.getenv("OPENAI_API_KEY")

    url = "https://openrouter.ai/api/v1/chat/completions"

    header = {
        "Autharization" : f"Bearer {openai_api}",
        "Content_Type" : "application/json"
    }

    response = requests.post(url, headers=header, json=data)

    if response.status_code in errors:
        return errors.get(response.status_code)

    return response["choices"][0]["message"]["content"]
