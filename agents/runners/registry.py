from agents.runners.python_runner import PythonRunner
from agents.runners.node_runner import NodeRunner

RUNNERS = {
    "python": PythonRunner(),
    "node": NodeRunner(),
}


def get_runner(project_type: str):
    return RUNNERS.get(project_type)