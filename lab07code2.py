from queue import PriorityQueue

# ---------- Graph 2 ----------
graph2 = {
    'S': [('A', 4), ('B', 10), ('C', 11)],
    'A': [('S', 4), ('B', 8), ('D', 5)],
    'B': [('S', 10), ('A', 8), ('C', 8), ('D', 15)],
    'C': [('S', 11), ('B', 8), ('E', 20), ('F', 2)],
    'D': [('A', 5), ('B', 15), ('H', 16), ('I', 20), ('F', 1)],
    'E': [('C', 20), ('G', 19)],
    'F': [('C', 2), ('D', 1), ('G', 13)],
    'H': [('D', 16), ('I', 1), ('J', 2)],
    'I': [('D', 20), ('H', 1), ('J', 5), ('G', 5), ('K', 13)],
    'J': [('H', 2), ('I', 5), ('K', 7)],
    'K': [('J', 7), ('I', 13), ('G', 16)],
    'G': []
}

# Heuristics from image
h2 = {
    'S': 7, 'A': 8, 'B': 6, 'C': 5, 'D': 5,
    'E': 3, 'F': 3, 'H': 7, 'I': 4, 'J': 5,
    'K': 3, 'G': 0
}


# -------- Best First Search ----------
def best_first_search(graph, start, goal, h):
    pq = PriorityQueue()
    pq.put((h[start], start))
    visited = set()
    path = []

    while not pq.empty():
        _, node = pq.get()
        if node in visited:
            continue

        visited.add(node)
        path.append(node)

        if node == goal:
            return path

        for neigh, _ in graph[node]:
            if neigh not in visited:
                pq.put((h[neigh], neigh))

    return None


# -------- Beam Search ----------
def beam_search(graph, start, goal, h, beam_width):
    frontier = [start]
    visited = set()
    path = []

    while frontier:
        visited.update(frontier)
        path.extend(frontier)

        if goal in frontier:
            return path

        candidates = []
        for node in frontier:
            for neigh, _ in graph[node]:
                if neigh not in visited:
                    candidates.append(neigh)

        candidates.sort(key=lambda x: h[x])
        frontier = candidates[:beam_width]

    return None


# -------- A* Search ----------
def astar(graph, start, goal, h):
    pq = PriorityQueue()
    pq.put((0 + h[start], 0, start, [start]))  # f, g, node, path
    visited = set()

    while not pq.empty():
        f, g, node, path = pq.get()

        if node == goal:
            return path, g

        if node in visited:
            continue
        visited.add(node)

        for neigh, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neigh]
            pq.put((new_f, new_g, neigh, path + [neigh]))

    return None


print("Graph-2 Best First Search Path:", best_first_search(graph2, 'S', 'G', h2))
print("Graph-2 Beam Search Path (width=2):", beam_search(graph2, 'S', 'G', h2, 2))
print("Graph-2 A* Result:", astar(graph2, 'S', 'G', h2))
