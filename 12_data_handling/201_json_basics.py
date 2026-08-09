import json

data = {"name": "Alice", "age": 30, "active": True, "scores": [90, 85, 92]}

json_string = json.dumps(data)
print("JSON string:", json_string)

json_pretty = json.dumps(data, indent=2)
print(json_pretty)

loaded = json.loads(json_string)
print(type(loaded))
print(loaded["name"])

nested = {"user": {"id": 1, "tags": ["python", "developer"]}}
print(json.dumps(nested, indent=2))

parsed = json.loads('{"x": 1, "y": [1, 2, 3]}')
print(parsed["y"])
