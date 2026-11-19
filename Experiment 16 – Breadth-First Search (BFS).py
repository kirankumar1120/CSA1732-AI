
from collections import deque

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3]
}

def bfs(start, end):
    q = deque([[start]])
    visited = set()

    while q:
        path = q.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    q.append(path + [n])

    return None

print("Shortest path:", bfs(0, 4))
