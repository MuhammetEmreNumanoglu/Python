def is_palindrome(text):
    cleaned = text.lower().replace(" ", "").replace(",", "").replace(".", "")
    return cleaned == cleaned[::-1]

tests = [
    "racecar",
    "hello",
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "Python",
    "level",
    "Madam Im Adam",
]

for text in tests:
    result = is_palindrome(text)
    print(f"'{text}': {result}")

def is_palindrome_number(n):
    s = str(abs(n))
    return s == s[::-1]

for num in [121, 1221, 123, -121, 0]:
    print(f"{num}: {is_palindrome_number(num)}")
