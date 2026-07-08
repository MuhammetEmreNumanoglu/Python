from collections import deque

dq = deque([1, 2, 3, 4, 5])

dq.append(6)
print(dq)

dq.appendleft(0)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

dq.rotate(2)
print(dq)

dq.rotate(-2)
print(dq)

limited = deque(maxlen=3)
for i in range(6):
    limited.append(i)
    print(limited)
