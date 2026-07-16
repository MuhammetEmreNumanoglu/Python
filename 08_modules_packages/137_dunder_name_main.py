def greet():
    print("Hello from greet()")

def main():
    print("Running as main script")
    greet()

print(f"__name__ is: {__name__}")

if __name__ == "__main__":
    main()
else:
    print("This module was imported, not run directly")
