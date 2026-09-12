import json
import os
import tempfile

CONTACTS_FILE = os.path.join(tempfile.gettempdir(), "contacts.json")

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE) as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(name, phone, email=""):
    contacts = load_contacts()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Added: {name}")

def find_contact(name):
    contacts = load_contacts()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info.get('email', 'N/A')}")
    else:
        print(f"'{name}' not found.")

def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts.")
        return
    for name, info in sorted(contacts.items()):
        print(f"{name}: {info['phone']}")

def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Deleted: {name}")
    else:
        print("Not found.")

add_contact("Alice", "555-1234", "alice@example.com")
add_contact("Bob", "555-5678")
add_contact("Charlie", "555-9012", "charlie@example.com")
list_contacts()
find_contact("Alice")
delete_contact("Bob")
list_contacts()

if os.path.exists(CONTACTS_FILE):
    os.remove(CONTACTS_FILE)
