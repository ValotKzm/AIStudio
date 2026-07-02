from models.task import Task

class Workflow:

    def __init__(self, agents):
        self.agents = agents

    def run(self, prompt: str, verbose: bool = False):

        task = Task(prompt=prompt)

        for agent in self.agents:

            if verbose:
                print(f"\n--- {agent.NAME.upper()} ---\n")

            previous_result = task.result

            agent.run(task)
            if verbose and task.result != previous_result:
                print(task.result)

        return task
    