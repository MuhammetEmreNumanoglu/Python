from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

def is_anagram_sort(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

pairs = [
    ("listen", "silent"),
    ("hello", "world"),
    ("anagram", "nagaram"),
    ("rat", "car"),
    ("Triangle", "Integral"),
    ("abc", "cba"),
]

for a, b in pairs:
    result = is_anagram(a, b)
    print(f"'{a}' & '{b}': {result}")

print("\nUsing sort method:")
for a, b in pairs:
    print(f"'{a}' & '{b}': {is_anagram_sort(a, b)}")
