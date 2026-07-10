import re

text = "Contact: john@example.com or jane@test.org"

pattern = r"(\w+)@(\w+)\.(\w+)"
matches = re.findall(pattern, text)
print(matches)

match = re.search(pattern, text)
if match:
    print("Full match:", match.group(0))
    print("User:", match.group(1))
    print("Domain:", match.group(2))
    print("TLD:", match.group(3))

named_pattern = r"(?P<user>\w+)@(?P<domain>\w+)\.(?P<tld>\w+)"
match = re.search(named_pattern, text)
if match:
    print("User:", match.group("user"))
    print("Domain:", match.group("domain"))

date = "2024-01-15"
date_match = re.match(r"(\d{4})-(\d{2})-(\d{2})", date)
if date_match:
    year, month, day = date_match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
