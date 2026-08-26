import traceback
import sys

def level3():
    raise ValueError("Something went wrong")

def level2():
    level3()

def level1():
    level2()

try:
    level1()
except ValueError:
    print("Full traceback:")
    traceback.print_exc()

print()

try:
    level1()
except ValueError:
    tb_str = traceback.format_exc()
    print("Traceback as string:")
    print(tb_str)

try:
    level1()
except ValueError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    frames = traceback.extract_tb(exc_tb)
    print("Frames:")
    for frame in frames:
        print(f"  File {frame.filename}, line {frame.lineno}, in {frame.name}")
