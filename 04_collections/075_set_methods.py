s = {1, 2, 3, 4, 5}

s.add(6)
print(s)

s.remove(3)
print(s)

s.discard(99)
print(s)

popped = s.pop()
print("Popped:", popped)

copy = s.copy()
s.clear()
print("Cleared:", s)
print("Copy:", copy)

numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)
