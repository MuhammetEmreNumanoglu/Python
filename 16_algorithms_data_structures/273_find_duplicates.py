def find_duplicates_set(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def find_duplicates_counter(items):
    from collections import Counter
    counts = Counter(items)
    return [item for item, count in counts.items() if count > 1]

data = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]
print("Duplicates (set method):", find_duplicates_set(data))
print("Duplicates (counter method):", find_duplicates_counter(data))

words = ["apple", "banana", "apple", "cherry", "banana", "date"]
print("Duplicate words:", find_duplicates_set(words))

unique = list(dict.fromkeys(data))
print("Unique (order preserved):", unique)
