from agents.runner import Runner
from models.task import Task


class PythonRunner(Runner):

    NAME = "Python Runner"

    def should_run(self, task: Task) -> bool:
        return any(
            file.suffix == ".py"
            for file in task.files
        )
    
    def execute(self, task: Task):
        
        print("Python project detected!")