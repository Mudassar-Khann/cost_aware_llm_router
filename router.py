from config import Config
from utils import contains_keywords

class Router:
    def __init__(self):
        self.complex_keywords = {
            "explain", "why", "how", "compare", "design"
        }

    def route(self, text: str):
        words = set(text.lower().split())

        if contains_keywords(words, self.complex_keywords):
            return {
                "model": Config.EFFCIENT_MODEL,
                "reason": "keyword_complex"
            }

        if len(words) > 20:
            return {
                "model": Config.EFFCIENT_MODEL,
                "reason": "long_query"
            }


        return {
            "model": Config.DEFAULT_MODEL,
            "reason": "default_simple"
        }
