from agents.runners.python_runner import PythonRunner

RUNNERS = {
    "python": PythonRunner(),
}


def get_runner(project_type: str):
    return RUNNERS.get(project_type)