from agents.developer import Developer
from agents.manager import Manager
from agents.tester import Tester

developer = Developer()
manager = Manager()
tester = Tester()

task = input("What would you like to do? ")

print("\n--- MANAGER ---\n")
plan = manager.run(task)
print(plan)

if plan == "The AI could not generate a response.":
    print("\nStopping workflow.")
    exit()

print("\n--- DEVELOPER ---\n")
code = developer.run(plan)
print(code)

print("\n--- TESTER ---\n")
review = tester.run(code)
print(review)
