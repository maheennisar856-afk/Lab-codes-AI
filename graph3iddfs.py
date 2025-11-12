# Graph for IDDFS
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}

def dls_iddfs(graph, node, goal, limit):
    if node == goal:
        return True
    if limit <= 0:
        return False
    for neighbor in graph[node]:
        if dls_iddfs(graph, neighbor, goal, limit - 1):
            return True
    return False

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Limit: {depth}")
        if dls_iddfs(graph, start, goal, depth):
            print(f"Goal {goal} found at depth {depth}")
            return True
    print("Goal not found")
    return False

print("\nIDDFS:")
iddfs(graph, 0, 5, 3)