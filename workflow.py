from models.task import Task
from agents.filewriter import FileWriter

class Workflow:

    def __init__(self, agents):
        self.agents = agents

    def run(self, prompt: str, verbose: bool = False):

        task = Task(prompt=prompt)

        for agent in self.agents:

            if not agent.should_run(task):
                continue

            if verbose:
                print(f"\n--- {agent.NAME.upper()} ---\n")

            previous_result = task.result

            agent.run(task)
            if verbose and task.result != previous_result:
                print(task.result)

        if task.metadata.get("needs_rewrite"):
            
            task.metadata["needs_rewrite"] = False

            FileWriter().run(task)

        return task
    