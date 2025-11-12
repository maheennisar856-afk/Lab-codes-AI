# Graph for DLS
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}

def dls(graph, node, goal, limit):
    print(f"Visiting: {node}, Limit: {limit}")
    if node == goal:
        return True
    if limit <= 0:
        return False
    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, limit - 1):
            return True
    return False

print("\nDLS (Depth Limit = 2):")
found = dls(graph, 0, 5, 2)
print("Goal Found!" if found else "Goal Not Found!")