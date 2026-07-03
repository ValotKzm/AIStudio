from pathlib import Path

from agents.agent import Agent
from llm.registry import get_provider
from models.task import Task

class LLMAgent(Agent):
    
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

    def build_prompt(self, task: Task) -> str:
        
        return task.result or task.prompt

    def run(self, task: Task):
        provider = get_provider(self.provider)

        prompt = self.build_prompt(task)

        task.result = provider.ask(
            self.model,
            self.system_prompt,
            prompt,
        )
