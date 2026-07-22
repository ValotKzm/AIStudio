from models.task import Task
from agents.filewriter import FileWriter
from agents.runners.registry import get_runner

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

                task.metadata["repair_attempts"] += 1
            
                task.metadata["needs_rewrite"] = False

                FileWriter().run(task)

        self._run_runner(task)

        while (
            task.metadata.get("return_code",0) != 0
            and task.metadata["repair_attempts"] < 3
        ):
            print(
                f"Repair attempt: "
                f"{task.metadata['repair_attempts'] + 1}"
            )
            self._run_fixer(task)

            if task.metadata.get("needs_rewrite"):

                task.metadata["repair_attempts"] += 1
                task.metadata["needs_rewrite"] = False

                FileWriter().run(task)

            self._run_runner(task)

        return task
        
    def _run_runner(self, task: Task):
        runner = get_runner(task.metadata.get("project_type"))

        if runner is None:
            print(
                f"No runner available for project type: "
                f"{task.metadata.get('project_type')}"
            )
            return

        runner.run(task)

    def _run_fixer(self, task: Task):

        for agent in self.agents:

            if agent.NAME != "Fixer":
                continue

            if not agent.should_run(task):
                return
            
            agent.run(task)
            return
