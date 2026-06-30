from .base_agent import BaseAgent


class Manager(BaseAgent):
    def __init__(self):
        super().__init__("prompts/manager.txt")
