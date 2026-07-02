word = "Python"

for char in word:
    print(char)

vowels = set("aeiouAEIOU")
for char in "Hello World":
    if char in vowels:
        print(char, end=" ")
print()

text = "abcde"
for char in reversed(text):
    print(char, end="")
print()
