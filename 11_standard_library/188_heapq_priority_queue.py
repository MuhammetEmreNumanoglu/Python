import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)

print("Heap:", heap)
print("Min:", heap[0])

while heap:
    print(heapq.heappop(heap), end=" ")
print()

tasks = [(3, "Low priority"), (1, "High priority"), (2, "Medium priority")]
heapq.heapify(tasks)

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"[{priority}] {task}")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("3 smallest:", heapq.nsmallest(3, numbers))
print("3 largest:", heapq.nlargest(3, numbers))
