def show_menu():
    print("\n--- Menu ---")
    print("1. Say Hello")
    print("2. Show current number")
    print("3. Quit")

number = 42

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        print("Hello, user!")
    elif choice == "2":
        print(f"Current number: {number}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again")
