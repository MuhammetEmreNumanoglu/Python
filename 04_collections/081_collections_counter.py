from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)

print(counter)
print(counter["apple"])
print(counter.most_common(2))

text = "hello world"
char_count = Counter(text)
print(char_count)

numbers = [1, 2, 1, 3, 2, 1, 4]
num_count = Counter(numbers)
print(num_count)
print(sum(num_count.values()))
