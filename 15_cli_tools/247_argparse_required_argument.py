import argparse

parser = argparse.ArgumentParser(description="Greet a user")
parser.add_argument("name", help="Name of the person to greet")
parser.add_argument("count", type=int, help="Number of times to greet")

args = parser.parse_args()

for _ in range(args.count):
    print(f"Hello, {args.name}!")
