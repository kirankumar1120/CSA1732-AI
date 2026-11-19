
def evaluate(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return 10 if board[a] == "X" else -10

    return 0


def alpha_beta(board, alpha, beta, is_max):
    score = evaluate(board)

    if score != 0 or " " not in board:
        return score

    if is_max:
        best = -1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, alpha_beta(board, alpha, beta, False))
                board[i] = " "
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = 1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, alpha_beta(board, alpha, beta, True))
                board[i] = " "
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best


board = ["X", "O", "X",
         "O", "O", " ",
         " ", " ", "X"]

best_score = -1000
best_move = -1

for i in range(9):
    if board[i] == " ":
        board[i] = "X"
        score = alpha_beta(board, -1000, 1000, False)
        board[i] = " "

        if score > best_score:
            best_score = score
            best_move = i

print("Best move for X:", best_move + 1)
