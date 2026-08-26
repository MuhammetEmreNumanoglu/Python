import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
print("Count:", len(sys.argv) - 1)

if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"  arg[{i}] = {arg}")
else:
    print("No arguments provided.")
    print("Usage: python 246_command_line_arguments.py arg1 arg2 ...")
