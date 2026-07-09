text = "Hello, World! Hello, Python!"

print(text.find("Hello"))
print(text.find("Java"))
print(text.rfind("Hello"))

print(text.count("Hello"))
print(text.count("l"))

new_text = text.replace("Hello", "Hi")
print(new_text)

replaced_once = text.replace("Hello", "Hi", 1)
print(replaced_once)

print(text.startswith("Hello"))
print(text.endswith("Python!"))

index = text.index("World")
print(index)
