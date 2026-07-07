fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()

print(fruits)
print(type(empty_set))
print(len(fruits))
print("apple" in fruits)
print("grape" in fruits)

fruits.add("date")
print(fruits)

fruits.discard("banana")
print(fruits)

unique = set([1, 2, 2, 3, 3, 3, 4])
print(unique)
