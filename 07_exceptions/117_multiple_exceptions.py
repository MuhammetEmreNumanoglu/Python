def risky(value):
    try:
        result = 10 / value
        items = [1, 2, 3]
        return items[int(result)]
    except ZeroDivisionError:
        print("Division by zero")
    except IndexError:
        print("Index error")
    except (TypeError, ValueError) as e:
        print(f"Type/Value error: {e}")

risky(0)
risky(3)
risky("x")

try:
    x = int("bad")
except (ValueError, TypeError):
    print("Caught either ValueError or TypeError")
