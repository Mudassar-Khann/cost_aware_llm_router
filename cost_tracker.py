from config import Config

class CostTracker:
    def __init__(self):
        self.total_cost = 0
        self.total_tokens = 0

    def update(self, model, usage):
        input_tokens = usage.prompt_tokens
        output_tokens = usage.completion_tokens

        pricing = Config.PRICING[model]

        cost = (
            (input_tokens / 1000) * pricing["input"] +
            (output_tokens / 1000) * pricing["output"]
        )

        self.total_cost += cost
        self.total_tokens += input_tokens + output_tokens

        return {
            "cost": cost,
            "total_cost": self.total_cost
        }
