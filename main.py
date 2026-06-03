from router import Router
from request_builder import RequestBuilder
from llm_client import LLMClient
from cost_tracker import CostTracker
from logger import get_logger
from config import Config
from errors import (RateLimitError, InvalidRequestError,
 NetworkError, TimeoutError, AuthenticationError, PermissionDeniedError, ModelNotFoundError, ProviderError)


logger = get_logger()

router = Router()
builder = RequestBuilder()
client = LLMClient()
tracker = CostTracker()

def main():
    print("App initialized. Type 'exit' to quit.\n")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Ending session.")
            break


        route = router.route(user_input)


        payload = builder.build(
            user_input=user_input,
            model=route["model"],
            mode="text"
        )

        for i in range(Config.MAX_RETRIES):

            result = client.send(payload)

            if result["success"]:
                break


            error = result["error"]

            logger.error(f"Message={error.message} Model: {error.model} Provider: {error.provider} Reason={error.cause_of_error} ")

            if isinstance(error, (AuthenticationError, InvalidRequestError, ModelNotFoundError)):
                print(f"Model: {error.model} \nProvider: {error.provider} \nReason={error.cause_of_error} ")
                break

            elif isinstance(error, PermissionDeniedError):
                 print(f"Model: {error.model} \nProvider: {error.provider} \nReason={error.cause_of_error} ")
                 print("Avalible Models")
                 for model in Config.MODELS:
                     if error.model == model:
                         print(f"> {model}")
                         continue
                     print(model)
                 chnage_model = input("Do you wanna change the model enter 'y' for yes and 'n' for no: ")
                 if chnage_model == "n":
                     break
                 chnage_to = input("write model name or press enter to change automatically: ")

                 if chnage_to:
                    if chnage_to in Config.MODELS:
                        if not Config.MODELS[chnage_to]["available"]:
                            print("You have to buy the plan to access this model")
                            break
                        payload["model"] = chnage_to

                    else:
                        print("typed Model is not available")
                        break
                 else:
                      if error.model == Config.DEFAULT_MODEL:
                           payload["model"] = Config.EFFCIENT_MODEL

                      else:
                           payload["model"] = Config.DEFAULT_MODEL



            elif isinstance(error,(NetworkError, TimeoutError, RateLimitError)):
                print(f"Model: {error.model} \nProvider: {error.provider} \nReason={error.cause_of_error} ")
                if i == 2:
                    print("There is some issue with server retry after some time")

                else:
                  print("retrying..")


            elif isinstance(error, ProviderError):
                print(f"{error.message} \nModel: {error.model} \nProvider: {error.provider} \nReason={error.cause_of_error} ")
                break


            elif isinstance(error, Exception):
                 print(f"Model: {error.model} \nProvider: {error.provider} \nReason={error.cause_of_error} ")
                 break



        if not result["success"]:
            continue


        data = result["data"]
        usage = data.usage


        content = data.choices[0].message.content




        cost_info = tracker.update(
            model=route["model"],
            usage= usage
        )

        logger.info(
            f"model={route['model']} "
            f"reason={route['reason']} "
            f"tokens={usage} "
            f"cost={cost_info['cost']:.6f}"
        )


        print(f"\n[MODEL] {route['model']}")
        print(f"{content}")
        print(f"[REASON] {route['reason']}")
        print(f"[TOKENS] {usage}")
        print(f"[COST] ${cost_info['cost']:.6f}")
        print(f"[TOTAL COST] ${cost_info['total_cost']:.6f}\n")


if __name__ == "__main__":
    main()
