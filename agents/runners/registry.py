from agents.runners.python_runner import PythonRunner
from agents.runners.node_runner import NodeRunner

RUNNERS = {
    PythonRunner.PROJECT_TYPE: PythonRunner(),
    NodeRunner.PROJECT_TYPE: NodeRunner(),
}


def get_runner(project_type: str):
    return RUNNERS.get(project_type)