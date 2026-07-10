print("hello".isalpha())
print("hello123".isalpha())
print("123".isdigit())
print("abc123".isdigit())
print("abc123".isalnum())
print("   ".isspace())
print("Hello World".istitle())
print("HELLO".isupper())
print("hello".islower())
print("".isalpha())

user_input = "Alice123"
if user_input.isalnum():
    print("Valid username")

pin = "4892"
if pin.isdigit() and len(pin) == 4:
    print("Valid PIN")
