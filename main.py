from router import ModelSelection
import llm_client
import time

ms = ModelSelection()


print("> Enter your 'query' for model response or type 'exist' to leave the sesstion: ")
while True:
    query = input(">").strip()
    star_time = time.perf_counter()

    if query == "exit":
        print("Ending sesstion..")
        break
    user_query = ms.selct_model(query)
    response = llm_client.send_response(user_query)
    end_time = time.perf_counter()

    if "takin too long" in response or "unavlible" in response:
        print("Server is busy retry after some time ")
        break

    print(f"Model : {response}")





