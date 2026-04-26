from dotenv import load_dotenv
import os
import requests
import logging
import logging


logger = logging.getLogger(__name__)


errors = {
    400 : "Api request is invalid somthing is missing fix your input",
    401 : "unauthorized tookes missing or wrong api",
    404 : "Model you requsted dosn't exist ",
    429 : "limit exceeded",
    500 : "sever error",
    503 : "service unavlible"
}


def send_response(data: dict, errors = errors):

    # return data

    if not data:
        return "can't give answer to empty message"

    load_dotenv()
    openai_api = os.getenv("OPENAI_API_KEY")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
    "Authorization": f"Bearer {openai_api}",
    "Content-Type": "application/json"
}



    try:
        response = requests.post(url, headers=headers, json=data, timeout=15.0)
        result = response.json()

        if response.ok:
            return result

    except requests.Timeout as e:
        return f"request taking too long: {e}"
    except Exception as e:
        return f"json error:", {e}

    if response.status_code in errors or response.status_code != 200:
        logging.error(f"server response: {response.status_code} {errors.get(response.status_code)}")
        return errors.get(response.status_code)

    if "choices" not in result:
        return f"unexpected response: {result}"






