def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

numbers = [4, 2, 7, 1, 9, 3, 8, 5, 6]

result = linear_search(numbers, 9)
print(f"Found 9 at index: {result}")

result = linear_search(numbers, 10)
print(f"Found 10 at index: {result}")

names = ["Alice", "Bob", "Charlie", "Dave"]
print(f"Found 'Charlie' at: {linear_search(names, 'Charlie')}")
print(f"Found 'Eve' at: {linear_search(names, 'Eve')}")
