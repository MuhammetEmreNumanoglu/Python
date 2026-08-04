import uuid

id1 = uuid.uuid4()
id2 = uuid.uuid4()
id3 = uuid.uuid4()

print(id1)
print(id2)
print(id3)
print(id1 == id2)

print(type(id1))
print(str(id1))
print(id1.hex)

user_id = str(uuid.uuid4())
session_id = str(uuid.uuid4())
print(f"User: {user_id}")
print(f"Session: {session_id}")

uid = uuid.UUID("550e8400-e29b-41d4-a716-446655440000")
print(uid)
print(uid.version)
