import subprocess
from pathlib import Path

from agents.runners.runner import Runner
from models.task import Task


class NodeRunner(Runner):

    NAME = "Node Runner"

    def should_run(self, task: Task) -> bool:
        return task.metadata.get("project_type") == "node"
    
    def execute(self, task: Task):

        entry_point = self._find_entry_point(task)

        if entry_point is None:
            print("No node entry point found.")
            return

        print(f"Running {entry_point.name}")

        command = [
            "node",
            str(entry_point),
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
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

    def _find_entry_point(self, task: Task) -> Path | None:

        for file in task.files:
            if file.name == "index.js":
                return file
            
        for file in task.files:
            if file.suffix == ".js":
                return file

        return None