import json
import os
import tempfile

TODO_FILE = os.path.join(tempfile.gettempdir(), "todos.json")

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE) as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_todo(title):
    todos = load_todos()
    todos.append({"title": title, "done": False})
    save_todos(todos)
    print(f"Added: {title}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos.")
        return
    for i, todo in enumerate(todos, 1):
        status = "x" if todo["done"] else " "
        print(f"[{status}] {i}. {todo['title']}")

def complete_todo(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        print(f"Completed: {todos[index - 1]['title']}")

add_todo("Learn Python")
add_todo("Build a project")
add_todo("Practice daily")
list_todos()
complete_todo(1)
list_todos()

if os.path.exists(TODO_FILE):
    os.remove(TODO_FILE)
