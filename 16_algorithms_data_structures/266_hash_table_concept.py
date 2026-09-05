class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        self.buckets[index] = [(k, v) for k, v in self.buckets[index] if k != key]

ht = HashTable()
ht.set("name", "Alice")
ht.set("age", 30)
ht.set("city", "London")

print(ht.get("name"))
print(ht.get("age"))
print(ht.get("email"))

ht.set("age", 31)
print(ht.get("age"))

ht.delete("city")
print(ht.get("city"))

print("\nPython dict is a hash table:")
d = {"name": "Alice", "age": 30}
print(d["name"])
