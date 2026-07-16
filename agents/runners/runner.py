from pathlib import Path
import subprocess

from agents.agent import Agent
from models.task import Task


class Runner(Agent):

    NAME = "Runner"

    PROJECT_TYPE = ""

    ENTRY_POINTS = ()

    EXTENSION = ""

    EXECUTABLE = ""

    def execute(self, task: Task):
        
        entry_point = self._find_entry_point(task)

        if entry_point is None:
            print(f"No {self.PROJECT_TYPE} entry point found.")
            return
        
        print(f"Running {entry_point.name}")

        command = [
            self.EXECUTABLE,
            entry_point.name,
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=entry_point.parent,
        )

        task.metadata["return_code"] = result.returncode
        task.metadata["stdout"] = result.stdout
        task.metadata["stderr"] = result.stderr

        if result.returncode == 0:
            print("Execution succeeded.")
        else:
            print("Execution failed.")

        if result.stdout:
            print("\n--- STDOUT ---")
            print(result.stdout)

        if result.stderr:
            print("\n--- STDERR ---")
            print(result.stderr)


    def run(self, task: Task):
        self.execute(task)

    def should_run(self, task: Task) -> bool:
        return task.metadata.get("project_type") == self.PROJECT_TYPE
    
    def _find_entry_point(self, task: Task) -> Path | None:

        for file in task.files:
            if file.name in self.ENTRY_POINTS:
                return file
        
        for file in task.files:
            if file.suffix == self.EXTENSION:
                return file
            
        return None