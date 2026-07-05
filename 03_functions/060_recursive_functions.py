def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def countdown(n):
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)

def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(factorial(6))
countdown(5)
print(sum_list([1, 2, 3, 4, 5]))
