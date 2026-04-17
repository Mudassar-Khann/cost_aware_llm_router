from router import ModelSelection
import llm_client

ms = ModelSelection()

print("> Enter your 'query' for model response or type 'exist' to leave the sesstion: ")
# while True:
query = input(">").strip()

if query == "exist":
    print("Ending sesstion..")
    # break
user_query = ms.selct_model(query)
response = llm_client.send_response(user_query)

print(f"Model : {response}")





