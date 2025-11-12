import heapq

# Weighted graph for Problem No. 1 (example costs)
graph = {
    0: [(1, 1), (2, 4), (3, 7)],   # (neighbor, cost)
    1: [(4, 3), (5, 1)],
    2: [(5, 2)],
    3: [],
    4: [],
    5: [(6, 5)],
    6: []
}

def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]  # (cost, current_node, path)
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node in visited:
            continue
        
        path = path + [node]
        visited.add(node)
        print(f"Visiting {node} with cost {cost}")
        
        if node == goal:
            print(f"\nGoal {goal} reached with total cost: {cost}")
            print(f"Path: {' -> '.join(map(str, path))}")
            return
        
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path))
    
    print(f"\nGoal {goal} not reachable from {start}")

# Example: find least-cost path from 0 to 6
ucs(graph, 0, 6)