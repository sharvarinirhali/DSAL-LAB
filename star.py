# A* Algorithm Implementation for Game Search Problem
# Example: Pathfinding on a grid

from heapq import heappop, heappush

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # cost from start
        self.h = 0  # heuristic (Manhattan distance)
        self.f = 0  # total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    end_node = Node(end)

    heappush(open_list, start_node)

    while open_list:
        current_node = heappop(open_list)
        closed_list.add(current_node.position)

        # Goal check
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # reverse path

        # Possible moves (up, down, left, right)
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        for move in moves:
            node_pos = (current_node.position[0] + move[0],
                        current_node.position[1] + move[1])

            # Check boundaries and obstacles
            if (0 <= node_pos[0] < len(grid) and
                0 <= node_pos[1] < len(grid[0]) and
                grid[node_pos[0]][node_pos[1]] == 0 and
                node_pos not in closed_list):

                child = Node(node_pos, current_node)
                child.g = current_node.g + 1
                child.h = heuristic(child.position, end_node.position)
                child.f = child.g + child.h

                # If already in open list with lower f, skip
                if any(open_node.position == child.position and open_node.f <= child.f for open_node in open_list):
                    continue

                heappush(open_list, child)

    return None

# Example grid (0 = free, 1 = obstacle)
grid = [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0]
]

start = (0,0)
end = (4,4)

path = astar(grid, start, end)
print("Path found:", path)
