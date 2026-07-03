from pathlib import Path

from agents.runner import Runner
from models.task import Task


class PythonRunner(Runner):

    NAME = "Python Runner"

    def should_run(self, task: Task) -> bool:
        return task.metadata.get("project_type") == "python"
    
    def execute(self, task: Task):

        entry_point = self._find_entry_point(task)

        if entry_point is None:
            print("No Python entry point found.")
            return

        print(f"Running {entry_point.name}")

    def _find_entry_point(self, task: Task) -> Path | None:

        for file in task.files:
            if file.name == "main.py":
                return file
            
        for file in task.files:
            if file.suffix == ".py":
                return file

        return None