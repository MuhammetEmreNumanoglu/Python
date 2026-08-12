from urllib.parse import urlparse, urlencode, urljoin, quote, unquote

url = "https://www.example.com:8080/path/to/page?name=Alice&age=30#section"

parsed = urlparse(url)
print("Scheme:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)
print("Query:", parsed.query)
print("Fragment:", parsed.fragment)

params = {"name": "Alice Smith", "city": "New York", "age": 30}
query_string = urlencode(params)
print("Query string:", query_string)

base = "https://example.com/docs/"
relative = "guide.html"
full = urljoin(base, relative)
print("Joined:", full)

text = "Hello World & Python!"
encoded = quote(text)
print("Encoded:", encoded)
print("Decoded:", unquote(encoded))
