import secrets

token = secrets.token_hex(16)
print("Hex token:", token)

token_bytes = secrets.token_bytes(16)
print("Bytes token:", token_bytes)

url_token = secrets.token_urlsafe(16)
print("URL-safe token:", url_token)

secure_num = secrets.randbelow(100)
print("Secure random (0-99):", secure_num)

choices = ["option_a", "option_b", "option_c"]
choice = secrets.choice(choices)
print("Secure choice:", choice)

otp = "".join([str(secrets.randbelow(10)) for _ in range(6)])
print("OTP:", otp)
