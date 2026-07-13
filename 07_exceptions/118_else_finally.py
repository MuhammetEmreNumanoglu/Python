def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("divide() finished")

divide(10, 2)
print()
divide(10, 0)
print()

import tempfile, os

temp = os.path.join(tempfile.gettempdir(), "finally_demo.txt")
try:
    f = open(temp, "w")
    f.write("test")
except IOError:
    print("IO Error")
finally:
    f.close()
    os.remove(temp)
    print("File closed and removed")
