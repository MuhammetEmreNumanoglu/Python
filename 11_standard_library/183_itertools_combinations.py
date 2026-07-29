import itertools

items = ["a", "b", "c", "d"]

combos_2 = list(itertools.combinations(items, 2))
print("C(4,2):", combos_2)
print("Count:", len(combos_2))

combos_3 = list(itertools.combinations(items, 3))
print("C(4,3):", combos_3)

with_replacement = list(itertools.combinations_with_replacement("abc", 2))
print("With replacement:", with_replacement)

numbers = [1, 2, 3, 4]
pairs = list(itertools.combinations(numbers, 2))
pair_sums = [(a + b, (a, b)) for a, b in pairs]
print("Pair sums:", pair_sums)
