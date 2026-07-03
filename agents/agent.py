from abc import ABC, abstractmethod
from models.task import Task

class Agent(ABC):

    NAME = "Agent"

    def should_run(self, task: Task) -> bool:
        return True

    @abstractmethod
    def run(self, task: Task):
        pass
    