from collections import Counter
import re

def count_words(text):
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words)

text = """
Python is great. Python is easy to learn.
Learning Python helps you build great projects.
Python Python Python!
"""

word_counts = count_words(text)

print("Word counts:")
for word, count in word_counts.most_common(5):
    print(f"  {word}: {count}")

print(f"\nTotal unique words: {len(word_counts)}")
print(f"Total words: {sum(word_counts.values())}")
print(f"'python' appears: {word_counts['python']} times")
