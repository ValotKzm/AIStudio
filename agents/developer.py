from .base_agent import BaseAgent
from config import settings


class Developer(BaseAgent):
    
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
