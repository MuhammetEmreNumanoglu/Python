import urllib.request
import json

url = "https://httpbin.org/json"

try:
    with urllib.request.urlopen(url, timeout=5) as response:
        status = response.status
        data = json.loads(response.read().decode())
        print("Status:", status)
        print("Data:", data)
except Exception as e:
    print("Request failed:", e)
    print("(This is expected if there is no internet connection.)")

try:
    with urllib.request.urlopen("https://httpbin.org/get?name=Alice", timeout=5) as r:
        result = json.loads(r.read().decode())
        print("Args:", result.get("args"))
except Exception as e:
    print("Second request failed:", e)
