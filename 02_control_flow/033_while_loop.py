count = 0
while count < 5:
    print(count)
    count += 1

number = 1
while number <= 32:
    number *= 2
print("Final:", number)

user_input = ""
attempts = 0
while user_input != "exit" and attempts < 3:
    user_input = input("Type 'exit' to stop: ")
    attempts += 1

print("Done after", attempts, "attempts")
