def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30, city="London")

def create_user(username, **options):
    user = {"username": username}
    user.update(options)
    return user

user = create_user("alice", role="admin", active=True, plan="pro")
print(user)

def mixed(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

mixed(1, 2, 3, name="Alice", age=30)
