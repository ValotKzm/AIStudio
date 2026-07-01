from .base_agent import BaseAgent
from config import settings


class Manager(BaseAgent):
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
