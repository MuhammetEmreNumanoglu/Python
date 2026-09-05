class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Stack after pop:", stack)
print("Size:", stack.size())

def is_balanced(text):
    stack = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

print(is_balanced("(hello [world])"))
print(is_balanced("((()))"))
print(is_balanced("([)]"))
