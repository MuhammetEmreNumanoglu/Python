numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

words = ["hello", "world", "python"]
uppercased = list(map(str.upper, words))
print(uppercased)

prices = [10.5, 20.0, 15.75]
with_tax = list(map(lambda p: round(p * 1.2, 2), prices))
print(with_tax)

names = ["alice", "bob", "charlie"]
lengths = list(map(len, names))
print(lengths)
