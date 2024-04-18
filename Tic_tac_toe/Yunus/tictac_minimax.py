import tkinter as tk
import tkinter.messagebox
import random

# Define the size of the game board
BOARD_SIZE = 3

# Define players
player, opponent = "X", "O"

# Function to check if there are available moves left
def isMoveLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == "_"):
                return True
    return False

# Evaluation function to determine the score of the board
def evaluate(b):
    # Check rows for X or O victory
    for row in range(0, 3):
        if b[row][0] == b[row][1] == b[row][2]:
            if b[row][0] == "X":
                return 10
            elif b[row][0] == "O":
                return -10
    # Check columns for X or O victory
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col]:
            if b[0][col] == "X":
                return 10
            elif b[0][col] == "O":
                return -10
    # Check diagonals for X or O victory
    if b[0][0] == b[1][1] == b[2][2]:
        if b[0][0] == "X":
            return 10
        elif b[0][0] == "O":
            return -10
    if b[0][2] == b[1][1] == b[2][0]:
        if b[0][2] == "X":
            return 10
        elif b[0][2] == "O":
            return -10
    # If none has won, return zero
    return 0

# Minimax algorithm implementation
def minimax(board, depth, isMax):
    score = evaluate(board)
    # If maximizer wins, return the score - depth
    if score == 10:
        return score - depth
    # If minimizer wins, return the score + depth
    if score == -10:
        return score + depth
    # If there are no more moves, it's a tie
    if not isMoveLeft(board):
        return 0
    # Maximizing player's move
    if isMax:
        best = -1000
        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if (board[i][j] == "_"):
                    # Make move
                    board[i][j] = player
                    # Call minimax recursively and choose the max value
                    best = max(best, minimax(board, depth + 1, not isMax))
                    # Undo move
                    board[i][j] = "_"
        return best
    # Minimizing player's move
    else:
        best = 1000
        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if (board[i][j] == "_"):
                    # Make move
                    board[i][j] = opponent
                    # Call minimax recursively and choose the min value
                    best = min(best, minimax(board, depth + 1, not isMax))
                    # Undo move
                    board[i][j] = "_"
        return best

# Function to return the best move for a player
def findBestMove(board, maximizing_player):
    bestVal = float('-inf') if maximizing_player else float('inf')
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                # Make a move
                board[i][j] = player if maximizing_player else opponent
                # Compute the evaluation function for this move
                moveVal = minimax(board, 0, not maximizing_player)
                # Undo the move
                board[i][j] = "_"
                # Update the best move and value based on the player type
                if maximizing_player and moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
                elif not maximizing_player and moveVal < bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

# Function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to check if a player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(cell != "_" for row in board for cell in row)

# Function for human player's move
def human_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == "_":
                return row, col
            else:
                print("That position is already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

# Function to play the game
def play_game():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    # Initialize the game board
    board = [["_"] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    def make_move(row, col):
        nonlocal board
        nonlocal is_maximizer_turn

        if board[row][col] == "_":
            symbol = "X" if is_maximizer_turn else "O"
            board[row][col] = symbol
            buttons[row][col].config(text=symbol)
            is_maximizer_turn = not is_maximizer_turn
            check_game_status()

            # If the game is not over and it's the AI's turn
            if not check_winner() and not check_draw() and not is_maximizer_turn:
                ai_row, ai_col = findBestMove(board, False)  # AI's move
                make_move(ai_row, ai_col)

    def check_game_status():
        nonlocal board
        winner = check_winner()
        if winner:
            tk.messagebox.showinfo("Game Over", f"{winner} wins!")
            reset_board()
        elif check_draw():
            tk.messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()

    def check_winner():
        nonlocal board
        for i in range(BOARD_SIZE):
            # Check rows
            if board[i][0] == board[i][1] == board[i][2] != "_":
                return board[i][0]
            # Check columns
            if board[0][i] == board[1][i] == board[2][i] != "_":
                return board[0][i]
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != "_":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "_":
            return board[0][2]
        return None

    def check_draw():
        nonlocal board
        return not is_winner(board, "X") and not is_winner(board, "O") and is_full(board)

    def reset_board():
        nonlocal board
        nonlocal is_maximizer_turn

        # Reset the game board and buttons
        board = [["_"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                buttons[i][j].config(text="")
        is_maximizer_turn = True

    # Create buttons for each cell in the game board
    buttons = [[None]*BOARD_SIZE for _ in range(BOARD_SIZE)]
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                                      command=lambda row=i, col=j: make_move(row, col))
            buttons[i][j].grid(row=i, column=j)

    is_maximizer_turn = True

    root.mainloop()

if __name__ == "__main__":
    play_game()