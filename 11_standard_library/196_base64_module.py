import base64

text = "Hello, World!"
encoded = base64.b64encode(text.encode())
print("Encoded:", encoded)
print("Encoded str:", encoded.decode())

decoded = base64.b64decode(encoded)
print("Decoded:", decoded.decode())

url_encoded = base64.urlsafe_b64encode(text.encode())
print("URL-safe encoded:", url_encoded.decode())

url_decoded = base64.urlsafe_b64decode(url_encoded)
print("URL-safe decoded:", url_decoded.decode())

data = b"\x00\x01\x02\x03\xff\xfe\xfd"
enc = base64.b64encode(data)
print("Binary encoded:", enc)
dec = base64.b64decode(enc)
print("Binary decoded:", dec)
