numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

words = ["apple", "fig", "banana", "kiwi", "cherry"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)

scores = [45, 78, 92, 55, 88, 30, 65]
passing = list(filter(lambda s: s >= 60, scores))
print(passing)

names = ["Alice", "", "Bob", "", "Charlie"]
non_empty = list(filter(None, names))
print(non_empty)
