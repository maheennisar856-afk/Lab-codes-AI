from collections import deque

# Graph Problem No. 1 (as shown in the image)
graph = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [5],
    3: [],
    4: [],
    5: [6],
    6: []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(i for i in graph[node] if i not in visited)

# Run BFS from node 0
bfs(graph, 0)