import os

path = os.environ.get("PATH", "Not set")
home = os.environ.get("HOME") or os.environ.get("USERPROFILE", "Unknown")
user = os.environ.get("USER") or os.environ.get("USERNAME", "Unknown")
lang = os.environ.get("LANG", "Not set")

print("HOME:", home)
print("USER:", user)
print("LANG:", lang)
print("PATH (first 100 chars):", path[:100])

os.environ["MY_APP_DEBUG"] = "true"
os.environ["MY_APP_PORT"] = "8080"

debug = os.environ.get("MY_APP_DEBUG", "false") == "true"
port = int(os.environ.get("MY_APP_PORT", "3000"))

print(f"\nApp Debug: {debug}")
print(f"App Port: {port}")

del os.environ["MY_APP_DEBUG"]
del os.environ["MY_APP_PORT"]
