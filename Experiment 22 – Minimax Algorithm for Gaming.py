
def evaluate(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return 10 if board[a] == "X" else -10

    return 0


def minimax(board, depth, is_max):
    score = evaluate(board)

    if score != 0 or " " not in board:
        return score

    if is_max:
        best = -1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, depth + 1, False))
                board[i] = " "
        return best

    else:
        best = 1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, depth + 1, True))
                board[i] = " "
        return best


board = ["X", "O", "X",
         "O", "O", " ",
         " ", " ", "X"]

best_score = -1000
best_move = -1

for i in range(9):
    if board[i] == " ":
        board[i] = "X"
        score = minimax(board, 0, False)
        board[i] = " "

        if score > best_score:
            best_score = score
            best_move = i

print("Best move for X:", best_move + 1)
