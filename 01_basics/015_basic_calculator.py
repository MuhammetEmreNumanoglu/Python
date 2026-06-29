a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

if b != 0:
    print(f"{a} / {b} = {a / b:.4f}")
else:
    print("Cannot divide by zero")
