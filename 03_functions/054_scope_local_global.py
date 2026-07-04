message = "I am global"

def read_global():
    print(message)

def create_local():
    local_message = "I am local"
    print(local_message)

read_global()
create_local()

x = 10

def show_x():
    print("x from outer scope:", x)

show_x()
print("x in global scope:", x)
