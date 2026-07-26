numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if (n := len(numbers)) > 5:
    print(f"List has {n} elements")

while (line := input("Enter text (or 'quit'): ")) != "quit":
    print("You entered:", line)

data = [1, 2, 3, 4, 5]
if (first := data[0]) > 0:
    print(f"First element is positive: {first}")

import re

text = "The price is 42 dollars"
if match := re.search(r"\d+", text):
    print("Found number:", match.group())
