value = None

print(value)
print(type(value))
print(value is None)
print(value is not None)

def get_user(user_id):
    if user_id == 1:
        return "Alice"
    return None

result = get_user(99)
if result is None:
    print("User not found")
else:
    print(result)
