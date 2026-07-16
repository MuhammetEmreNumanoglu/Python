import sys

print("Python version:", sys.version)
print("Version info:", sys.version_info)
print("Platform:", sys.platform)
print("Executable:", sys.executable)
print("Module search paths:", sys.path[:3])
print("Argv:", sys.argv)
print("Recursion limit:", sys.getrecursionlimit())
print("Default encoding:", sys.getdefaultencoding())
print("Max int:", sys.maxsize)

sys.setrecursionlimit(2000)
print("New recursion limit:", sys.getrecursionlimit())
