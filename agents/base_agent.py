from pathlib import Path
from llm import ask

class BaseAgent:
    
    def __init__(self, prompt_file):

        self.system_prompt = Path(prompt_file).read_text(
            encoding="utf-8"
        )

    def run(self, task):

        return ask(
            self.system_prompt,
            task
        )
        