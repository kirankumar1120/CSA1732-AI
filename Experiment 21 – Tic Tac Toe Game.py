
board = [' '] * 9

def display():
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        if i < 6:
            print("-----")

def win(p):
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == p for i in line)
               for line in lines)

while ' ' in board:
    display()

    for p in ['X', 'O']:
        while True:
            pos = int(input(f"Player {p}, enter position (1-9): ")) - 1
            if 0 <= pos < 9 and board[pos] == ' ':
                board[pos] = p
                break
            print("Invalid position! Try again.")

        if win(p):
            display()
            print(p, "Wins!")
            break

    if win('X') or win('O'):
        break
else:
    display()
    print("It's a Draw!")
