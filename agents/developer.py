from .base_agent import BaseAgent


class Developer(BaseAgent):
    
    def __init__(self):
        super().__init__("prompts/developer.txt")
