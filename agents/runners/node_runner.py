from agents.runners.runner import Runner

class NodeRunner(Runner):

    NAME = "Node Runner"

    PROJECT_TYPE = "node"

    ENTRY_POINTS = (
        "index.js",
    )

    EXTENSION = ".js"

    EXECUTABLE = "node"
