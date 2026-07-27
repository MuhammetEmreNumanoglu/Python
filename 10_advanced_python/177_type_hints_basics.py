def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def repeat(text: str, times: int = 1) -> str:
    return text * times

def process(items: list, limit: int = 10) -> list:
    return items[:limit]

print(greet("Alice"))
print(add(3, 5))
print(repeat("ha", 3))
print(process([1, 2, 3, 4, 5]))

print(greet.__annotations__)
print(add.__annotations__)
