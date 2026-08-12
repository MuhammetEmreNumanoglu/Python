import json

MOCK_API_RESPONSE = """
{
  "status": "ok",
  "results": [
    {"id": 1, "title": "Python is great", "author": "Alice"},
    {"id": 2, "title": "Learn JSON APIs", "author": "Bob"},
    {"id": 3, "title": "Mock data is useful", "author": "Charlie"}
  ],
  "total": 3
}
"""

def parse_api_response(json_str):
    data = json.loads(json_str)
    return data

def get_titles(data):
    return [item["title"] for item in data["results"]]

def get_by_author(data, author):
    return [item for item in data["results"] if item["author"] == author]

data = parse_api_response(MOCK_API_RESPONSE)
print("Status:", data["status"])
print("Total:", data["total"])
print("Titles:", get_titles(data))
print("By Alice:", get_by_author(data, "Alice"))
