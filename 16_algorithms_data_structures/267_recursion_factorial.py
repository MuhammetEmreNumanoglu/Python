def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

for i in range(11):
    print(f"{i}! = {factorial(i)}")

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iterative(10))
