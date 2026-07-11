import os
import tempfile

log_file = os.path.join(tempfile.gettempdir(), "log.txt")

with open(log_file, "w") as f:
    f.write("Session started\n")

with open(log_file, "a") as f:
    f.write("User logged in\n")

with open(log_file, "a") as f:
    f.write("Action performed\n")
    f.write("User logged out\n")

with open(log_file, "r") as f:
    print(f.read())

os.remove(log_file)
