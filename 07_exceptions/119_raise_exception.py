def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistically high")
    return age

try:
    set_age(-1)
except ValueError as e:
    print(f"Error: {e}")

try:
    set_age(200)
except ValueError as e:
    print(f"Error: {e}")

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dividing by zero is not allowed")
    return a / b

try:
    divide(5, 0)
except ZeroDivisionError as e:
    print(f"Caught: {e}")
