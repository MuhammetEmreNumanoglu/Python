import hashlib

text = "Hello, World!"

md5 = hashlib.md5(text.encode()).hexdigest()
print("MD5:", md5)

sha1 = hashlib.sha1(text.encode()).hexdigest()
print("SHA1:", sha1)

sha256 = hashlib.sha256(text.encode()).hexdigest()
print("SHA256:", sha256)

sha512 = hashlib.sha512(text.encode()).hexdigest()
print("SHA512:", sha512[:32], "...")

password = "my_secure_password"
hashed = hashlib.sha256(password.encode()).hexdigest()
print("Hashed password:", hashed)

print("Available algorithms:", sorted(hashlib.algorithms_available)[:5])
