name = "Alice"
age = 30
balance = 1234567.89
items = ["apple", "banana", "cherry"]

print(f"{name!r}")
print(f"{name!s}")
print(f"{name!a}")

print(f"{balance:,.2f}")
print(f"{balance:>20,.2f}")
print(f"{0.005:.1%}")
print(f"{255:#010b}")
print(f"{255:#x}")

width = 10
print(f"{'left':<{width}}|")
print(f"{'right':>{width}}|")

import datetime
today = datetime.date.today()
print(f"{today:%B %d, %Y}")

x = 42
print(f"{x = }")
