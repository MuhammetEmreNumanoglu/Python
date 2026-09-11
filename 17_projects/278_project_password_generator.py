import secrets
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    required = []

    if use_upper:
        chars += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        required.append(secrets.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*"
        chars += symbols
        required.append(secrets.choice(symbols))

    remaining = length - len(required)
    password_chars = required + [secrets.choice(chars) for _ in range(remaining)]

    shuffled = list(password_chars)
    for i in range(len(shuffled) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    return "".join(shuffled)

for i in range(5):
    pwd = generate_password(16)
    print(f"Password {i + 1}: {pwd}")

print("\nSimple 8-char (letters only):", generate_password(8, use_digits=False, use_symbols=False))
print("Strong 20-char:", generate_password(20))
