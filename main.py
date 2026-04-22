from router import ModelSelection
import llm_client
import time

ms = ModelSelection()


print("> Enter your 'query' for model response or type 'exist' to leave the session: ")
while True:
    query = input(">").strip()


    if query == "exit":
        print("Ending session..")
        break
    user_query = ms.select_model(query)
    response = llm_client.send_response(user_query)

    print(f"Model : {response["choices"][0]["message"]["content"]}")
    print(f"[Tokens] : input={response["usage"].get("prompt_tokens", "info not avalibal")}  output={response["usage"].get("completion_tokens", "info not avalibal")}, total={response["usage"].get("total_tokens", "info not avalibal")}")





