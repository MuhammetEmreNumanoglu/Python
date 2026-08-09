import pickle
import tempfile
import os

data = {
    "name": "Alice",
    "scores": [90, 85, 92],
    "active": True,
}

tmp = os.path.join(tempfile.gettempdir(), "data.pkl")

with open(tmp, "wb") as f:
    pickle.dump(data, f)

with open(tmp, "rb") as f:
    loaded = pickle.load(f)

print(loaded)
print(loaded["name"])
print(loaded["scores"])

serialized = pickle.dumps([1, 2, 3, "hello"])
print(type(serialized))

deserialized = pickle.loads(serialized)
print(deserialized)

os.remove(tmp)
