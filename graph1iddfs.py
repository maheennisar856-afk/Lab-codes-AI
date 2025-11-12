# Graph Problem No. 1
graph = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [5],
    3: [],
    4: [],
    5: [6],
    6: []
}

def dls(graph, node, goal, limit, visited=None):
    if visited is None:
        visited = set()

    print(node, end=' ')
    visited.add(node)

    if node == goal:
        print("\nGoal found!")
        return True

    if limit <= 0:
        return False

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, goal, limit - 1, visited):
                return True
    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\n--- Depth Limit: {depth} ---")
        if dls(graph, start, goal, depth):
            print(f"Goal {goal} found at depth {depth}")
            return
    print(f"\nGoal {goal} not found within depth limit {max_depth}")

# Example run
iddfs(graph, 0, 6, 5)