import argparse

parser = argparse.ArgumentParser(description="A simple demo program")
parser.add_argument("name", help="Your name")
parser.add_argument("--age", type=int, default=0, help="Your age")
parser.add_argument("--verbose", action="store_true", help="Verbose output")

args = parser.parse_args()

if args.verbose:
    print(f"Running in verbose mode")

print(f"Hello, {args.name}!")

if args.age > 0:
    print(f"You are {args.age} years old.")
