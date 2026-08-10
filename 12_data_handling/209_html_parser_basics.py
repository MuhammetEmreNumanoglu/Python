from html.parser import HTMLParser

class SimpleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.headings = []
        self._current_tag = None

    def handle_starttag(self, tag, attrs):
        self._current_tag = tag
        if tag == "a":
            for attr, value in attrs:
                if attr == "href":
                    self.links.append(value)

    def handle_data(self, data):
        if self._current_tag in ("h1", "h2", "h3") and data.strip():
            self.headings.append((self._current_tag, data.strip()))

html = """
<html>
<body>
<h1>Welcome</h1>
<p>Visit <a href="https://python.org">Python</a> and <a href="https://docs.python.org">Docs</a>.</p>
<h2>Features</h2>
<ul><li>Simple</li><li>Powerful</li></ul>
</body>
</html>
"""

parser = SimpleParser()
parser.feed(html)

print("Links:", parser.links)
print("Headings:", parser.headings)
