from .llm_agent import LLMAgent
from models.task import Task
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

    def build_prompt(self, task: Task) -> str:

        parts = []

        for file in task.files:
            
            parts.append(f"FILE: {file.name}\n")
            content = file.read_text(
            encoding="utf-8",
            )

            parts.append(content)

        return "\n\n".join(parts)
    