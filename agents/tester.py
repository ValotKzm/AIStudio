from .base_agent import BaseAgent
from config import settings


class Tester(BaseAgent):
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
