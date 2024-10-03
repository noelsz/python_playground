board = [' ' for _ in range(9)]

def board_visual():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])
    print(f"\n{row1}\n{row2}\n{row3}\n")

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    while True:
        print(f"Player {number}'s turn")
        choice = int(input("Enter your move (1-9): ").strip())
        if board[choice - 1] == ' ':
            board[choice - 1] = icon
            break
        else:
            print(f"\nThe space is taken..")
            board_visual()

def victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def draw():
    if ' ' not in board:
        return True
    else:
        return False

# Game
while True:
    board_visual()
    player_move('X')
    board_visual()
    if victory('X'):
        board_visual()
        print("Player 1 wins!")
        break
    elif draw():
        board_visual()
        print("Draw!")
        break
    player_move('O')
    if victory('O'):
        board_visual()
        print("Player 2 wins!")
        break


