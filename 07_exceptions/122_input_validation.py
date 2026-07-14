def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("That's not a valid integer. Try again.")

def get_choice(options):
    print("Options:", ", ".join(options))
    while True:
        choice = input("Choose: ").strip().lower()
        if choice in options:
            return choice
        print(f"Invalid choice. Pick from: {options}")

number = get_positive_integer("Enter a positive integer: ")
print(f"You entered: {number}")

choice = get_choice(["yes", "no", "maybe"])
print(f"You chose: {choice}")
