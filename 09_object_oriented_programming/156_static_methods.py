class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def clamp(value, min_val, max_val):
        return max(min_val, min(value, max_val))

print(MathUtils.add(3, 5))
print(MathUtils.is_even(4))
print(MathUtils.is_even(7))
print(MathUtils.clamp(15, 0, 10))

m = MathUtils()
print(m.add(10, 20))

class StringUtils:
    @staticmethod
    def is_palindrome(text):
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]

print(StringUtils.is_palindrome("racecar"))
print(StringUtils.is_palindrome("A man a plan a canal Panama"))
print(StringUtils.is_palindrome("hello"))
