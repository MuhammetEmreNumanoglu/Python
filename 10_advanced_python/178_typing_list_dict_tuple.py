from typing import List, Dict, Tuple, Set

def total(numbers: List[int]) -> int:
    return sum(numbers)

def get_scores() -> Dict[str, int]:
    return {"Alice": 90, "Bob": 85}

def get_point() -> Tuple[int, int]:
    return (3, 5)

def unique_items(data: List[str]) -> Set[str]:
    return set(data)

print(total([1, 2, 3, 4, 5]))
print(get_scores())
print(get_point())
print(unique_items(["a", "b", "a", "c"]))

names: List[str] = ["Alice", "Bob", "Charlie"]
config: Dict[str, int] = {"timeout": 30, "retries": 3}
point: Tuple[int, int] = (10, 20)

print(names)
print(config)
print(point)
