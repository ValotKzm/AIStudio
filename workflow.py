class Workflow:

    def __init__(self, agents):
        self.agents = agents

    def run(self, task, verbose=False):

        result = task

        for agent in self.agents:
            print(f"\n--- {agent.NAME.upper()} ---\n")

            result= agent.run(result)

            print(result)

        return result