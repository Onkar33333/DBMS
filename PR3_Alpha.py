import math

# Initialize an empty 3x3 Tic-Tac-Toe board
board = [[' ']*3 for _ in range(3)]

def is_winner(board, player):
    # Check rows, columns, and diagonals for a winning combination
    return any(all(board[i][j] == player for i in range(3)) for j in range(3)) or \
           any(all(board[i][j] == player for j in range(3)) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3))

def is_draw(board):
    # Check if the board is full, indicating a draw
    return all(cell != ' ' for row in board for cell in row)

def evaluate(board):
    # Evaluate the board for 'X' or 'O' win, or a draw
    if is_winner(board, 'X'):
        return 1
    elif is_winner(board, 'O'):
        return -1
    return 0

def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main game loop
current_player = 'X'
while True:
    for row in board:
        print(' | '.join(row))
    if current_player == 'X':
        row, col = find_best_move(board)
        board[row][col] = 'X'
    else:
        print("Enter the row and column (0-2) for 'O':")
        row, col = map(int, input().split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

    if is_winner(board, current_player):
        for row in board:
            print(' | '.join(row))
        print(current_player, "wins!")
        break
    elif is_draw(board):
        for row in board:
            print(' | '.join(row))
        print("It's a draw!")
        break

    current_player = 'X' if current_player == 'O' else 'O'
