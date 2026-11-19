
from collections import deque

def valid(m, c):
    mr, cr = 3-m, 3-c
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (mr == 0 or mr >= cr))

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(2,0), (0,2), (1,1), (1,0), (0,1)]

    q = deque([(start, [start])])
    visited = {start}

    while q:
        (m, c, b), path = q.popleft()

        if (m, c, b) == goal:
            return path

        for x, y in moves:
            if b:
                new = (m-x, c-y, 0)
            else:
                new = (m+x, c+y, 1)

            if valid(new[0], new[1]) and new not in visited:
                visited.add(new)
                q.append((new, path + [new]))

    return []

solution = solve()

print("Solution:")
for state in solution:
    print(state)
