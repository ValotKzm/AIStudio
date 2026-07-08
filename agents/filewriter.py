from pathlib import Path

from agents.agent import Agent
from models.task import Task


class FileWriter(Agent):

    NAME = "File Writer"
    WORKSPACE = Path("workspace")

    def run(self, task: Task):

        task.metadata["project_type"] = self._extract_project_type(task.result)

        files = self._extract_files(task.result)

        if not files:
            print("No files found to write.")
            return

        self._write_files(files, task)

    def _extract_project_type(self, text: str) -> str:

        for line in text.splitlines():
            line = line.strip()

            if line.startswith("PROJECT:"):
                return line.replace("PROJECT:", "").strip()

        return "unknown"

    def _extract_files(self, text: str) -> list[tuple[str, str]]:

        files = []

        for block in text.split("FILE:")[1:]:

            lines = block.strip().splitlines()

            if not lines:
                continue

            filename = lines[0].replace("FILE:", "").strip()

            code_start = None

            for i, line in enumerate(lines):
                if line.strip().startswith("```"):
                    code_start = i
                    break

            if code_start is None:
                code = "\n".join(lines[1:])
            else:
                code = "\n".join(lines[code_start + 1 : -1])

            files.append((filename, code))

        return files

    def _write_files(
        self,
        files: list[tuple[str, str]],
        task: Task,
    ):

        self.WORKSPACE.mkdir(exist_ok=True)

        for filename, content in files:

            filepath = self.WORKSPACE / filename

            filepath.parent.mkdir(parents=True, exist_ok=True)

            filepath.write_text(
                content,
                encoding="utf-8",
            )

            task.files.append(filepath)

            print(f"Created: {filepath}")