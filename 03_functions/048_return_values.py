def add(a, b):
    return a + b

def square(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

def min_max(numbers):
    return min(numbers), max(numbers)

result = add(10, 5)
print(result)
print(square(7))
print(is_even(4))
print(is_even(7))

low, high = min_max([3, 1, 9, 5, 2])
print(low, high)
