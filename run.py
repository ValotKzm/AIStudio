from agents.developer import Developer
from agents.manager import Manager
from agents.tester import Tester
from agents.filewriter import FileWriter
from agents.python_runner import PythonRunner
from workflow import Workflow

workflow = Workflow([
    Manager(),
    Developer(),
    FileWriter(),
    PythonRunner(),
    Tester(),
])

task = input("What would you like to do? ")

result = workflow.run(task, verbose=True)
