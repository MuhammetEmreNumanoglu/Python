def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

def repeat(text: str, times: int = 1) -> str:
    return text * times

print(add(3, 5))
print(greet("Alice"))
print(repeat("ha", 3))

print(add.__annotations__)
