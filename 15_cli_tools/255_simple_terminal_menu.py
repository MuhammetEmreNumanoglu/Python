def show_menu(options, title="Menu"):
    print(f"\n=== {title} ===")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print(f"  0. Exit")
    print("=" * (len(title) + 8))

def get_choice(max_option):
    while True:
        try:
            choice = int(input("Enter choice: "))
            if 0 <= choice <= max_option:
                return choice
            print(f"Please enter 0-{max_option}")
        except ValueError:
            print("Enter a number")

options = ["Check time", "Say hello", "Show info"]

while True:
    show_menu(options, "Simple Terminal Menu")
    choice = get_choice(len(options))

    if choice == 0:
        print("Goodbye!")
        break
    elif choice == 1:
        import datetime
        print("Time:", datetime.datetime.now().strftime("%H:%M:%S"))
    elif choice == 2:
        name = input("Your name: ")
        print(f"Hello, {name}!")
    elif choice == 3:
        import sys
        print(f"Python {sys.version}")
