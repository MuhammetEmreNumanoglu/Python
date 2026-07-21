numbers = [1, 2, 3]
word = "hello"
my_range = range(5)

print(hasattr(numbers, "__iter__"))
print(hasattr(numbers, "__next__"))

it = iter(numbers)
print(hasattr(it, "__next__"))

print(next(it))
print(next(it))
print(next(it))

word_iter = iter(word)
for char in word_iter:
    print(char, end=" ")
print()

for x in range(3):
    print(x, end=" ")
print()

it2 = iter(range(3))
print(iter(it2) is it2)
