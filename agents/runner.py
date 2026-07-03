from abc import abstractmethod

from agents.agent import Agent
from models.task import Task


class Runner(Agent):

    @abstractmethod
    def execute(self, task: Task):
        pass

    def run(self, task: Task):
        self.execute(task)
