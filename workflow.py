class Workflow:

    def __init__(self, agents):
        self.agents = agents

    def run(self, task):

        result = task

        for agent in self.agents:
            result= agent.run(result)

        return result