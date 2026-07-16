import sys

from agents.runners.runner import Runner
from models.task import Task


class PythonRunner(Runner):

    NAME = "Python Runner"

    PROJECT_TYPE = "python"

    ENTRY_POINTS = (
        "main.py",
    )

    EXTENSION = ".py"

    EXECUTABLE = sys.executable
