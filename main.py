from router import Router
from request_builder import RequestBuilder
from llm_client import LLMClient
from cost_tracker import CostTracker
from logger import get_logger

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

        result = client.send(payload)

        if not result["success"]:
            print(f"[ERROR] {result['error']}")
            logger.error(result["error"])
            continue

        stream = result["data"]
        usage = stream.usage


        try:

            for chunk in  stream:

                contnet = chunk.choices[0].delta.content

                if contnet:

                    print(contnet, end="")


        finally:
            stream.close()



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
        print(f"[REASON] {route['reason']}")
        print(f"[TOKENS] {usage}")
        print(f"[COST] ${cost_info['cost']:.6f}")
        print(f"[TOTAL COST] ${cost_info['total_cost']:.6f}\n")


if __name__ == "__main__":
    main()
