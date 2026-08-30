import argparse

parser = argparse.ArgumentParser(description="Log level selector")
parser.add_argument(
    "--level",
    choices=["debug", "info", "warning", "error"],
    default="info",
    help="Log level",
)
parser.add_argument(
    "--format",
    choices=["text", "json", "csv"],
    default="text",
    help="Output format",
)

args = parser.parse_args()

print(f"Level: {args.level}")
print(f"Format: {args.format}")
print(f"Running with --level={args.level} --format={args.format}")
