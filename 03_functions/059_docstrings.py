def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area as a float.
    """
    import math
    return math.pi * radius ** 2

def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print(calculate_area(5))
print(calculate_area.__doc__)
print(divide(10, 2))
