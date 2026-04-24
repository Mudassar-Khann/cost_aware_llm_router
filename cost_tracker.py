
class CostTracker:

    def __init__(self):
        self.total_queries = 0
        self.total_cost = 0
        self.total_tokens = 0


    def cost_calculator(self, tokens, cost):
        if tokens or cost:
            self.total_queries += 1
            self.total_cost += cost
            self.total_tokens += tokens










