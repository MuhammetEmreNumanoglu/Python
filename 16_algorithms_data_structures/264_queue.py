from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek at empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(list(self._items))

q = Queue()
q.enqueue("first")
q.enqueue("second")
q.enqueue("third")

print("Queue:", q)
print("Peek:", q.peek())
print("Dequeue:", q.dequeue())
print("Queue after dequeue:", q)
print("Size:", q.size())
