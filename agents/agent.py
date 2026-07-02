from abc import ABC, abstractmethod
from models.task import Task

class Agent(ABC):

    NAME = "Agent"

    @abstractmethod
    def run(self, task: Task):
        pass