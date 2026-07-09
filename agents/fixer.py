from .llm_agent import LLMAgent
from models.task import Task
from config import settings


class Fixer(LLMAgent):

    NAME = "Fixer"

    def __init__(
        self,
        provider: str = settings.default_provider,
        model: str = settings.default_model,
    ):
        super().__init__(
            "prompts/fixer.txt",
            provider,
            model,
        )

    def should_run(self, task: Task) -> bool:
        return task.metadata.get("return_code", 0) != 0
    
    def build_prompt(self, task: Task) -> str:
        
        prompt = ""

        prompt += "The generated project failed during execution.\n\n"

        prompt += f"Return code: {task.metadata['return_code']}\n\n"

        prompt += "STDOUT:\n"
        prompt += task.metadata["stdout"]
        prompt += "\n\n"

        prompt += "STDERR:\n"
        prompt += task.metadata["stderr"]
        prompt += "\n\n"

        prompt += "Project files:\n\n"

        for file in task.files:

            prompt += f"FILE: {file.name}\n"

            content = file.read_text(
                encoding="utf-8",
            )

            prompt += content
            prompt += "\n\n"
        
        prompt += (
            "\n"
            f"Project type: {task.metadata['project_type']}\n\n"
            "Fix the project.\n"
            "Return ONLY the modified files using the required format."
        )

        return prompt
    
    def run(self, task: Task):

        super().run(task)

        task.metadata["needs_rewrite"] = True