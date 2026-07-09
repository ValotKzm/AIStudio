from agents.developer import Developer
from agents.manager import Manager
from agents.tester import Tester
from agents.filewriter import FileWriter
from agents.python_runner import PythonRunner
from agents.fixer import Fixer
from workflow import Workflow

workflow = Workflow([
    Manager(),
    Developer(),
    FileWriter(),
    Tester(),
    PythonRunner(),
    Fixer(),
])

task = input("What would you like to do? ")

result = workflow.run(task, verbose=True)
