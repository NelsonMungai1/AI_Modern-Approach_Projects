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

def findBestMove(board):
    bestVal=-1000
    bestMove=(-1,-1)
    # traverse all the cells, evaluate minimax function for all empty cells and Retunr the cell with optimal value
    for i in range(3):
        for j in range(3):
            # check if cell is empty
            if(board[i][j]=="_"):
                # make move 
                board[i][j]=player
                # compute evaluation function for this move
                moveVal=minimax(board,0,False)

                # undo move
                board[i][j]="_"

                # if value of current move is more than best value, then update best
                if(moveVal>bestVal):
                    bestMove=(i,j)
                    bestVal=moveVal

    # print("The value of the best Move is :",bestVal)
    # print()

    return bestMove
