text = "   Hello, World!   "

print(repr(text.strip()))
print(repr(text.lstrip()))
print(repr(text.rstrip()))

path = "///home/user///"
print(path.strip("/"))

padded = "***Hello***"
print(padded.strip("*"))
print(padded.lstrip("*"))
print(padded.rstrip("*"))

lines = ["  line 1  ", "  line 2  ", "  line 3  "]
cleaned = [line.strip() for line in lines]
print(cleaned)
