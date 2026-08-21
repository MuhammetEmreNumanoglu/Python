def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def clamp(value, low, high):
    return max(low, min(value, high))

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 3) == 7

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True

def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(15, 0, 10) == 10

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_is_palindrome()
    test_clamp()
    print("All tests passed!")
