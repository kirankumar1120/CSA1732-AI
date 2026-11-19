
import numpy as np

def tsp(cities):
    n = len(cities)
    tour = [0]
    unvisited = set(range(1, n))
    distance = 0

    while unvisited:
        current = tour[-1]
        nearest = min(
            unvisited,
            key=lambda i: np.linalg.norm(cities[current] - cities[i])
        )
        distance += np.linalg.norm(cities[current] - cities[nearest])
        tour.append(nearest)
        unvisited.remove(nearest)

    distance += np.linalg.norm(cities[tour[-1]] - cities[0])
    tour.append(0)

    return tour, distance

cities = np.array([[0, 0], [2, 3], [5, 4], [6, 1]])

route, distance = tsp(cities)

print("Best route:", route)
print("Total distance:", round(distance, 2))
