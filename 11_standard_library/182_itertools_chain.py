import itertools

a = [1, 2, 3]
b = ["a", "b", "c"]
c = [True, False]

chained = list(itertools.chain(a, b, c))
print(chained)

nested = [[1, 2], [3, 4], [5, 6]]
flat = list(itertools.chain.from_iterable(nested))
print(flat)

words = [["hello", "world"], ["foo", "bar"]]
all_words = list(itertools.chain.from_iterable(words))
print(all_words)

product = list(itertools.product([1, 2], ["a", "b"]))
print(product)
