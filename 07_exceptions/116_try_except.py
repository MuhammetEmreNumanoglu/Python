try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    number = int("abc")
except ValueError:
    print("Invalid number format")

try:
    items = [2,4,6]
    print(items[10])
except IndexError:
    print("Index out of range")

print("Program continues after exception")
