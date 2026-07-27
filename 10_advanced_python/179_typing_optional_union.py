from typing import Optional, Union

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

def parse_number(value: Union[str, int, float]) -> float:
    return float(value)

result = find_user(1)
if result is not None:
    print("Found:", result)

missing = find_user(99)
print("Missing:", missing)

print(parse_number("3.14"))
print(parse_number(42))
print(parse_number(1.5))

def get_name(obj: Optional[str] = None) -> str:
    return obj or "Anonymous"

print(get_name())
print(get_name("Alice"))
