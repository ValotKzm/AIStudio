from agents.runners.python_runner import PythonRunner
from agents.runners.node_runner import NodeRunner


RUNNER_CLASSES = (
    PythonRunner,
    NodeRunner,
)

RUNNERS = {
    runner.PROJECT_TYPE: runner()
    for runner in RUNNER_CLASSES
}


def get_runner(project_type: str):
    return RUNNERS.get(project_type)
