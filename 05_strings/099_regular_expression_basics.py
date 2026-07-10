import re

text = "My phone is 123-456-7890 and backup is 098-765-4321"

match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print("Found:", match.group())

all_phones = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print("All phones:", all_phones)

email = "user@example.com"
if re.match(r"[\w.]+@\w+\.\w+", email):
    print("Valid email")

cleaned = re.sub(r"\d", "#", "Call 123-456")
print(cleaned)

words = re.split(r"\s+", "Hello   World   Python")
print(words)
