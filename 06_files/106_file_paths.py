import os

cwd = os.getcwd()
print("Current directory:", cwd)

home = os.path.expanduser("~")
print("Home directory:", home)

joined = os.path.join(home, "Documents", "file.txt")
print("Joined path:", joined)

print("Basename:", os.path.basename(joined))
print("Dirname:", os.path.dirname(joined))
print("Split:", os.path.split(joined))
print("Extension:", os.path.splitext(joined))

print("Exists:", os.path.exists(home))
print("Is dir:", os.path.isdir(home))
print("Is file:", os.path.isfile(joined))
