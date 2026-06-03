from router import Router
from request_builder import RequestBuilder
from llm_client import LLMClient
from cost_tracker import CostTracker
from logger import get_logger
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

        for i in range(3):

            result = client.send(payload)

            if result["success"]:
                break

            error = result["error"]
            if isinstance(error, (AuthenticationError, RateLimitError, InvalidRequestError, ModelNotFoundError, PermissionDeniedError)):
                raise error

            elif isinstance(error,(NetworkError, TimeoutError)):
                print(f"{error.message} \nModel: {error.model} \nProvider: {error.provider} \nReason={error.cause_of_error} ")
                if i == 2:
                    print("There is some issue with server retry after some time")

                else:
                  print("retrying..")


            elif isinstance(error, ProviderError):
                print(f"{error.message} \nModel: {error.model} \nProvider: {error.provider} \nReason={error.cause_of_error} ")


            elif isinstance(error, Exception):
                raise error

            logger.error(f"Message={error.message} Model: {error.model} Provider: {error.provider} Reason={error.cause_of_error} ")

        if not result["success"]:
            break


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
