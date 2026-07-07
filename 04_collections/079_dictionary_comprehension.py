squares = {x: x ** 2 for x in range(10)}
print(squares)

words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

scores = {"Alice": 45, "Bob": 82, "Charlie": 60, "Dave": 35}
passing = {name: score for name, score in scores.items() if score >= 60}
print(passing)

inverted = {v: k for k, v in word_lengths.items()}
print(inverted)

keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(combined)
