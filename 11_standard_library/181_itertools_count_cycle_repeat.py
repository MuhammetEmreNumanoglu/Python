import itertools

counter = itertools.count(1)
for _ in range(5):
    print(next(counter), end=" ")
print()

counter_step = itertools.count(10, 5)
for _ in range(5):
    print(next(counter_step), end=" ")
print()

cycler = itertools.cycle(["red", "green", "blue"])
for _ in range(7):
    print(next(cycler), end=" ")
print()

repeater = itertools.repeat("hello", 4)
print(list(repeater))

numbers = [1, 2, 3]
repeated_list = list(itertools.repeat(numbers, 3))
print(repeated_list)
