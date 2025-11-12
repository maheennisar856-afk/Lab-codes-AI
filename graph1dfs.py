# Graph Problem No. 1 (same as used in BFS)
graph = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [5],
    3: [],
    4: [],
    5: [6],
    6: []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=' ')
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Run DFS from node 0
dfs(graph, 0)