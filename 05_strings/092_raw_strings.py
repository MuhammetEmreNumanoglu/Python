path = r"C:\Users\Alice\Documents\file.txt"
print(path)

pattern = r"\d+\.\d+"
print(pattern)

windows_path = r"C:\new_folder\test"
print(windows_path)

import re
text = "Price: 19.99 dollars"
match = re.search(r"\d+\.\d+", text)
if match:
    print("Found:", match.group())
