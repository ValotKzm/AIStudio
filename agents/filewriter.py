from pathlib import Path

from agents.agent import Agent
from models.task import Task


class FileWriter(Agent):

    NAME = "File Writer"

    WORKSPACE = Path("workspace")

    def run(self, task: Task):

        files = self._extract_files(task.result)

        if not files:
            print("No files found to write.")
            return

        self._write_files(files)

    def _extract_files(self, text: str) -> list[tuple[str, str]]:

        files = []

        for block in text.split("FILE:")[1:]:

            lines = block.strip().splitlines()

            filename = lines[0].strip()

            start = next(
                i for i, line in enumerate(lines)
                if line.startswith("```")
            ) + 1

            end = len(lines) - 1

            code = "\n".join(lines[start:end])

            files.append((filename, code))

        return files

    def _write_files(self, files: list[tuple[str, str]]):

        self.WORKSPACE.mkdir(exist_ok=True)

        for filename, content in files:

            filepath = self.WORKSPACE / filename

            filepath.write_text(
                content,
                encoding="utf-8",
            )

            print(f"Created: {filepath}")