# Depth First Search (DFS) and Breadth First Search (BFS)
# Undirected Graph Implementation

from collections import deque

# Graph represented as adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

# Recursive DFS
def dfs_recursive(node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(neighbor, visited)

# BFS using queue
def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Driver code
print("DFS Traversal (recursive):")
dfs_recursive(0, set())

print("\nBFS Traversal:")
bfs(0)
