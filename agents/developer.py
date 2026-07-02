from .llm_agent import LLMAgent
from config import settings


class Developer(LLMAgent):
    NAME = "Developer"

    def __init__(
        self,
        provider: str = settings.default_provider, 
        model: str = settings.default_model,
    ):
        super().__init__(
            "prompts/developer.txt",
            provider,
            model,
        )
