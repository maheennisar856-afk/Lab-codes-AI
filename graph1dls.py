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

# Example: search from node 0 to 6 with depth limit
limit = 3
print(f"DLS traversal (limit = {limit}):")
found = dls(graph, 0, 6, limit)

if not found:
    print("\nGoal not found within depth limit.")