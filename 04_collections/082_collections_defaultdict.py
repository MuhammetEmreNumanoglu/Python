from collections import defaultdict

word_groups = defaultdict(list)
words = [("fruit", "apple"), ("veggie", "carrot"), ("fruit", "banana"), ("veggie", "broccoli")]

for category, item in words:
    word_groups[category].append(item)

print(dict(word_groups))

count = defaultdict(int)
text = "hello world"
for char in text:
    count[char] += 1

print(dict(count))

graph = defaultdict(set)
graph["A"].add("B")
graph["A"].add("C")
graph["B"].add("C")
print(dict(graph))
