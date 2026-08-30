import argparse

parser = argparse.ArgumentParser(description="File processor")
parser.add_argument("filename", help="File to process")
parser.add_argument("--output", "-o", default="output.txt", help="Output file")
parser.add_argument("--verbose", "-v", action="store_true", help="Verbose mode")
parser.add_argument("--lines", "-n", type=int, default=10, help="Number of lines")

args = parser.parse_args()

if args.verbose:
    print(f"Processing: {args.filename}")
    print(f"Output: {args.output}")
    print(f"Lines: {args.lines}")

print(f"Would process '{args.filename}' and save to '{args.output}'")
