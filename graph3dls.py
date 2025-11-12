graph = {
    'A': ['B', 'C', 'E'],
    'B': ['D'],
    'C': ['F', 'I', 'E'],
    'D': ['H'],
    'E': ['H', 'J'],
    'F': [],
    'H': [],
    'I': ['J', 'G'],
    'J': ['G'],
    'G': []
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

limit = 3
print(f"\n\nDLS (limit={limit}) from A to G:")
found = dls(graph, 'A', 'G', limit)
if not found:
    print("\nGoal not found within depth limit.")