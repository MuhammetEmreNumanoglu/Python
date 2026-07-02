colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)

for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")

tasks = ["write code", "run tests", "deploy"]
for num, task in enumerate(tasks, start=1):
    print(f"Task {num}: {task}")
