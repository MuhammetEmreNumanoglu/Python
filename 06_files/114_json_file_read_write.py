import json
import tempfile
import os

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"],
    "address": {"city": "London", "zip": "EC1A"},
}

file_path = os.path.join(tempfile.gettempdir(), "data.json")

with open(file_path, "w") as f:
    json.dump(data, f, indent=2)

print("Written.")

with open(file_path, "r") as f:
    loaded = json.load(f)

print(loaded)
print(loaded["name"])
print(loaded["hobbies"])
print(loaded["address"]["city"])

os.remove(file_path)
