import os

print("CWD:", os.getcwd())
print("Platform:", os.name)

home = os.path.expanduser("~")
print("Home:", home)

print("PATH exists:", os.path.exists(home))

env_path = os.environ.get("PATH", "")
print("PATH length:", len(env_path))

print("PID:", os.getpid())

files = os.listdir(os.getcwd())
print("Files in CWD:", len(files))

joined = os.path.join("folder", "subfolder", "file.txt")
print("Joined:", joined)
