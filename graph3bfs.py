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
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(i for i in graph[node] if i not in visited)

print("BFS traversal from A:")
bfs(graph, 'A')