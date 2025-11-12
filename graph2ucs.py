import heapq

# Weighted Graph for UCS
graph = {
    0: [(1, 2), (2, 4)],
    1: [(3, 1), (4, 3)],
    2: [(5, 2), (6, 5)],
    3: [],
    4: [],
    5: [],
    6: []
}

def ucs(graph, start, goal):
    visited = set()
    pq = [(0, start, [])]  # (cost, node, path)
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        print(f"Visiting {node} with cost {cost}")
        
        if node == goal:
            print(f"\nGoal {goal} found with total cost {cost}")
            print(f"Path: {' -> '.join(map(str, path))}")
            return
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path))

print("\nUCS (0 to 5):")
ucs(graph, 0, 5)