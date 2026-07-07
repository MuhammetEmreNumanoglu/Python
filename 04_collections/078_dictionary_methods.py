config = {"host": "localhost", "port": 5432}

print(config.get("host"))
print(config.get("password", "not set"))

config.setdefault("timeout", 30)
print(config)

config.update({"port": 3306, "user": "admin"})
print(config)

removed = config.pop("timeout")
print("Removed:", removed)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}
print(merged)

copy = config.copy()
config.clear()
print("Cleared:", config)
print("Copy:", copy)
