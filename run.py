from agents.developer import Developer
from agents.manager import Manager
from agents.tester import Tester
from workflow import Workflow

workflow = Workflow([
    Manager(),
    Developer(),
    Tester(),
])

task = input("What would you like to do? ")

result = workflow.run(task)

print(result)
