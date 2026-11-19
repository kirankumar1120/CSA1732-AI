
from queue import PriorityQueue

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(3):
        for j in range(3):
            tile = state[i * 3 + j]

            if tile != 0:
                x = (tile - 1) // 3
                y = (tile - 1) % 3

                distance += abs(x - i) + abs(y - j)

    return distance


def successors(state):
    result = []
    i = state.index(0)

    moves = [-1, 1, -3, 3]

    for move in moves:
        new_pos = i + move

        if 0 <= new_pos < 9:
            if move == -1 and i % 3 == 0:
                continue
            if move == 1 and i % 3 == 2:
                continue

            new_state = list(state)
            new_state[i], new_state[new_pos] = (
                new_state[new_pos], new_state[i]
            )

            result.append(tuple(new_state))

    return result


def solve(initial_state):
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state), initial_state))

    explored = set()

    while not frontier.empty():
        _, state = frontier.get()

        if state == goal_state:
            print("Puzzle solved!")
            return

        if state in explored:
            continue

        explored.add(state)

        for next_state in successors(state):
            if next_state not in explored:
                priority = heuristic(next_state) + len(explored)
                frontier.put((priority, next_state))

    print("Puzzle unsolvable!")


initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)

solve(initial_state)
