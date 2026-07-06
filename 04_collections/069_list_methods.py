items = [3, 1, 4, 1, 5, 9, 2, 6]

items.append(7)
print(items)

items.insert(0, 0)
print(items)

items.remove(1)
print(items)

last = items.pop()
print("Popped:", last)
print(items)

print("Count of 1:", items.count(1))
print("Index of 9:", items.index(9))

items.sort()
print("Sorted:", items)

items.reverse()
print("Reversed:", items)

copy = items.copy()
items.clear()
print("Cleared:", items)
print("Copy:", copy)
