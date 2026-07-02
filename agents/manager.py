from .llm_agent import LLMAgent
from config import settings


class Manager(LLMAgent):
    NAME = "Manager"
    
    def __init__(
        self, 
        provider: str = settings.default_provider, 
        model: str = settings.default_model,
    ):
        super().__init__(
            "prompts/manager.txt",
            provider,
            model,
        )
