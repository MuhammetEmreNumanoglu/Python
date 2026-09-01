import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")

print(f"Username: {username}")
print(f"Password received (length: {len(password)})")

if username == "admin" and password == "secret":
    print("Login successful!")
else:
    print("Invalid credentials.")
