from .base_agent import BaseAgent


class Tester(BaseAgent):

    def __init__(self):
        super().__init__("prompts/tester.txt")
