from router import ModelSelection
from config import Config
import llm_client

ms = ModelSelection()


print("> Enter your 'query' for model response or type 'exist' to leave the session: ")
while True:
    query = input(">").strip()


    if query == "exit":
        print("Ending session..")
        break
    user_query = ms.select_model(query)
    response = llm_client.send_response(user_query)

    model = response.get("model")
    input_tokens = response["usage"].get("prompt_tokens", 0)
    output_tokens = response["usage"].get("completion_tokens", 0 )

    input_price = Config.Models_Token_Pricing[model].get("cost_per_1m_input", 0)
    output_price = Config.Models_Token_Pricing[model].get("cost_per_1m_output", 0)

    cost = ((input_price / 1000000) * input_tokens) + ((output_price / 1000000) * output_tokens)

    print(f"[Model] : {model}")
    print(f"[Model Response] : {response["choices"][0]["message"]["content"]} \n")
    print(f"[Tokens] : input={response["usage"].get("prompt_tokens", "info not avalibal")}  output={response["usage"].get("completion_tokens", "info not avalibal")}, total={response["usage"].get("total_tokens", "info not avalibal")}")
    print(f"[Cost] : {cost}$")





