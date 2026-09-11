from collections import defaultdict, deque

graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

add_edge(graph, "A", "B")
add_edge(graph, "A", "C")
add_edge(graph, "B", "D")
add_edge(graph, "C", "D")
add_edge(graph, "D", "E")

print("Adjacency list:")
for node, neighbors in sorted(graph.items()):
    print(f"  {node}: {sorted(neighbors)}")

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in sorted(graph[node]):
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in sorted(graph[start]):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

print("\nBFS from A:", bfs(graph, "A"))
print("DFS from A:", dfs(graph, "A"))
