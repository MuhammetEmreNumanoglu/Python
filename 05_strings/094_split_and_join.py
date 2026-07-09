sentence = "The quick brown fox"
words = sentence.split()
print(words)

csv_line = "Alice,30,London"
parts = csv_line.split(",")
print(parts)

path = "/home/user/documents/file.txt"
components = path.split("/")
print(components)

words = ["Python", "is", "fun"]
print(" ".join(words))
print("-".join(words))
print("\n".join(words))

items = ["apple", "banana", "cherry"]
print(", ".join(items))

text = "one::two::three"
print(text.split("::"))
print(text.split("::", 1))
