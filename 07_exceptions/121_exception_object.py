try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(type(e))
    print(str(e))
    print(e.args)

try:
    int("abc")
except ValueError as e:
    print(type(e).__name__)
    print(e)

try:
    open("/nonexistent/file.txt")
except OSError as e:
    print(f"Error code: {e.errno}")
    print(f"Message: {e.strerror}")
    print(f"Filename: {e.filename}")

import sys

try:
    1 / 0
except Exception:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print("Type:", exc_type.__name__)
    print("Value:", exc_value)
