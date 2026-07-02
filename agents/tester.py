from .llm_agent import LLMAgent
from config import settings


class Tester(LLMAgent):
    NAME = "Tester"

    def __init__(
        self,
        provider: str = settings.default_provider,
        model: str = settings.default_model,
    ):
        super().__init__(
            "prompts/tester.txt",
            provider,
            model,
        )
