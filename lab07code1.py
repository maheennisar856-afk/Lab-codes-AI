from queue import PriorityQueue

# ---------- Graph 1 ----------
graph1 = {
    'a': [('b', 9), ('c', 4), ('d', 7)],
    'b': [('a', 9), ('e', 11)],
    'c': [('a', 4), ('e', 17), ('f', 12)],
    'd': [('a', 7), ('f', 14)],
    'e': [('b', 11), ('c', 17), ('z', 5)],
    'f': [('c', 12), ('d', 14), ('z', 9)],
    'z': []
}

# Heuristic values (from image)
h1 = {
    'a': 21, 'b': 14, 'c': 18, 'd': 18,
    'e': 5, 'f': 8, 'z': 0
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


# -------- Beam Search (width = k) ----------
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


print("Graph-1 Best First Search Path:", best_first_search(graph1, 'a', 'z', h1))
print("Graph-1 Beam Search Path (width=2):", beam_search(graph1, 'a', 'z', h1, 2))
