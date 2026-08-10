import xml.etree.ElementTree as ET

xml_data = """<?xml version="1.0"?>
<library>
    <book id="1">
        <title>Python Crash Course</title>
        <author>Eric Matthes</author>
        <year>2023</year>
    </book>
    <book id="2">
        <title>Fluent Python</title>
        <author>Luciano Ramalho</author>
        <year>2022</year>
    </book>
</library>"""

root = ET.fromstring(xml_data)
print("Root tag:", root.tag)

for book in root.findall("book"):
    book_id = book.get("id")
    title = book.find("title").text
    author = book.find("author").text
    print(f"[{book_id}] {title} by {author}")
