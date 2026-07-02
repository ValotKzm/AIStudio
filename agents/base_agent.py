from pathlib import Path

from llm.registry import get_provider
from models.task import Task

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

    def run(self, task: Task):
        provider = get_provider(self.provider)

        task.result = provider.ask(
            self.model,
            self.system_prompt,
            task.result or task.prompt,
        )
