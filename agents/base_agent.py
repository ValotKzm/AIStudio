from pathlib import Path
from llm.registry import get_provider

class BaseAgent:
    
    def __init__(
            self,
            prompt_file: str,
            provider: str,
            model: str,
        ):

        self.system_prompt = Path(prompt_file).read_text(
            encoding="utf-8"
        )
        self.provider = provider
        self.model = model

    def run(self, task):
        provider = get_provider(self.provider)
        return provider.ask(
            self.model,
            self.system_prompt,
            task
        )
