
import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

h = {'A': 3, 'B': 2, 'C': 2, 'D': 1, 'E': 1, 'F': 0}

def astar(start, goal):
    q = [(h[start], 0, start, [start])]
    visited = set()

    while q:
        f, cost, node, path = heapq.heappop(q)

        if node == goal:
            return path, cost

        if node in visited:
            continue
        visited.add(node)

        for n in graph[node]:
            if n not in visited:
                new_cost = cost + 1
                heapq.heappush(
                    q, (new_cost + h[n], new_cost, n, path + [n])
                )

    return None, None

path, cost = astar('A', 'F')
print("Shortest path:", path)
print("Cost:", cost)
