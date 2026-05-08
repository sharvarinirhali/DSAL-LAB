# Prim's Minimal Spanning Tree Algorithm
# Greedy approach

INF = 9999999

# Number of vertices in graph
V = 5

# Graph represented as adjacency matrix
# 0 means no edge
G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

# Array to track selected vertices
selected = [False] * V

# Initially select the first vertex
selected[0] = True
edge_count = 0

print("Edge : Weight")

while edge_count < V - 1:
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j]:
                    # If edge exists and is smaller than current minimum
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(f"{x} - {y} : {G[x][y]}")
    selected[y] = True
    edge_count += 1
