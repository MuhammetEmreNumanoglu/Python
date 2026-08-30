import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: cannot divide by zero")
        return None
    return a / b

parser = argparse.ArgumentParser(description="CLI Calculator")
parser.add_argument("a", type=float, help="First number")
parser.add_argument("b", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation")

args = parser.parse_args()

operations = {"add": add, "sub": subtract, "mul": multiply, "div": divide}
result = operations[args.operation](args.a, args.b)

if result is not None:
    print(f"{args.a} {args.operation} {args.b} = {result}")
