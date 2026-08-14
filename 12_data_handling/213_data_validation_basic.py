import re

def validate_email(email):
    pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_age(age):
    return isinstance(age, int) and 0 <= age <= 150

def validate_username(username):
    return isinstance(username, str) and 3 <= len(username) <= 20 and username.isalnum()

def validate_user(data):
    errors = []
    if not validate_email(data.get("email", "")):
        errors.append("Invalid email")
    if not validate_age(data.get("age", -1)):
        errors.append("Invalid age")
    if not validate_username(data.get("username", "")):
        errors.append("Invalid username")
    return errors

users = [
    {"email": "alice@example.com", "age": 30, "username": "alice123"},
    {"email": "bad-email", "age": -5, "username": "ab"},
    {"email": "bob@test.org", "age": 25, "username": "bob"},
]

for user in users:
    errors = validate_user(user)
    if errors:
        print(f"Invalid: {errors}")
    else:
        print(f"Valid: {user['username']}")
