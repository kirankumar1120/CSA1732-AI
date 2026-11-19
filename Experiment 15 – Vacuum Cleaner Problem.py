
grid = [
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 0]
]

visited = set()

def clean(x, y):
    if (x, y) in visited:
        return

    visited.add((x, y))

    if grid[x][y] == 1:
        grid[x][y] = 0
        print("Cleaned:", (x, y))

    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 4 and 0 <= ny < 4:
            clean(nx, ny)

clean(0, 0)

print("The room is cleaned.")
