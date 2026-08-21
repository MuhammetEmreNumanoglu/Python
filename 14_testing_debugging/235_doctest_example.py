def add(a, b):
    """
    Add two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b

def is_even(n):
    """
    Return True if n is even.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    >>> is_even(0)
    True
    """
    return n % 2 == 0

def reverse_string(s):
    """
    Return the reversed string.

    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("")
    ''
    """
    return s[::-1]

if __name__ == "__main__":
    import doctest
    results = doctest.testmod(verbose=True)
    print(f"\nPassed: {results.attempted - results.failed}/{results.attempted}")
