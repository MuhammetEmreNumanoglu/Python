text = "Python"
width = 20

print(text.ljust(width))
print(text.rjust(width))
print(text.center(width))

print(text.ljust(width, "-"))
print(text.rjust(width, "-"))
print(text.center(width, "-"))

number = "42"
print(number.zfill(8))
print("3.14".zfill(10))

headers = ["Name", "Age", "City"]
values = ["Alice", "30", "London"]

for h, v in zip(headers, values):
    print(f"{h:<10} {v:<10}")
