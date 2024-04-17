#Algorithms Explained-minimax and alpha-beta prunning bu Sebastian Lague.
# Geek for Geeks and implementing its for tic tac toe


def play_game():
    board = [["_"] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        # Maximizing AI's turn
        print("Maximizer's turn (AI):")
        row, col = findBestMove(board)
        board[row][col] = "X"
        print_board(board)
        if is_winner(board, "X"):
            print("Maximizer wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        # Minimizing AI's turn
        print("Minimizer's turn (AI):")
        row, col = findBestMove(board)
        board[row][col] = "O"
        print_board(board)
        if is_winner(board, "O"):
            print("Minimizer wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
