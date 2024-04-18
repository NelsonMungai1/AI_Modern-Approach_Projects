"""
function alpha_beta(node,depth,isMaximzingPlayer,alpha,beta):
    if node is leaf node:
        return value of the node
    if isMaximizerPlayer:
        bestVal=-INF
        for each child node:
            value=minimax(node,depth+1,false,alpha,beta)
            bestVal=max(bestVal,value)
            alpha=max(alpha,bestVal)
            if beta<=alpha:
                break
        return bestVal
    else:
        bestVal=+INF
        for each child node:
            value=minimax(node,depth+1,true,beta,alpha)
            bestVal=min(value,bestVal)
            beta=min(beta,bestVal)
            if beta<=alpha:
                break
        return bestVal


init call 
alpha_beta(0,0,true,-INF,INF)

"""
player,opponent="X","O"
# return true if available moves
def isMoveLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j]=="_"):
                return True
    return False

""" X as the maximizer if we win (+10)and O as the minimiser if win (-10) if draw=(0)"""

def evaluate(b):
    # check for rows for x or O victory
    for row in range(0,3):
        if b[row][0]==b[row][1] and b[row][1]==b[row][2]:
            if b[row][0]=="X":
                return 10
            elif b[row][0]=="O":
                return -10
    # checking columns for X or O victory
    for col in range(3):
        if b[0][col]==b[1][col] and b[1][col]==b[2][col]:
            if b[0][col]=="X":
                return 10
            elif b[0][col]=="O":
                return -10
    # checking for diagonals for X or O victory
    if b[0][0]==b[1][1] and b[1][1]==b[2][2]:
        if b[0][0]=="X":
            return 10
        elif b[0][0]=="O":
            return -10
    if b[0][2]==b[1][1] and b[1][1]==b[2][0]:
        if b[0][2]=="X":
            return 10
        elif b[0][2]=="O":
            return -10
    # if none has won the game return zero
    return 0

# Driver code 
        
def minimax(board,depth,isMax,alpha,beta):
    score=evaluate(board)
    # if maximier  wins game returns his/her evaluated score
    if(score==10):
        return score-depth
    
    # if minimizer has won game returns his/her evaluated score
    if(score==-10):
        return score+depth
    # /if there are no more moves tie
    if(isMoveLeft(board)==False):
        return 0
    # maximizer move
    if(isMax):
        best=-1000
        # traverse all cells
        for i in range(3):
            for j in range(3):

                # check if cell is empty
                if (board[i][j]=="_"):
                    # make move
                    board[i][j]=player
                    # call minimax recursively and chooe max value
                    best = max(best, minimax(board, depth + 1, not isMax, alpha, beta))
                    alpha = max(alpha, best)
                    board[i][j]="_"
                    if beta <= alpha:
                        break
                    # undo move
                    
        return best
    # for the minimizer
    else:
        best=1000
        # traverse all cells
        for i in range(3):
            for j in range(3):
                # check if cell is empty
                if(board[i][j]=="_"):
                    # make move
                    board[i][j]=opponent
                    # call minimax recursively and choose min value
                    best = min(best, minimax(board, depth + 1, not isMax, alpha, beta))
                    beta = min(beta, best)
                    board[i][j]="_"
                    if beta <= alpha:
                        break
                    # undo move
                    
        return best
    
# function to return best move for nplayer
def findBestMove(board, maximizing_player, alpha, beta):
    bestVal = float('-inf') if maximizing_player else float('inf')
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                # Make a move
                board[i][j] = player if maximizing_player else opponent
                # Compute the evaluation function for this move
                moveVal = minimax(board, 0, not maximizing_player, alpha, beta)
                # Undo the move
                board[i][j] = "_"
                # Update the best move and value based on the player type
                if maximizing_player:
                    if moveVal > bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal
                    alpha = max(alpha, bestVal)  # Update alpha based on bestVal
                    if beta <= alpha:
                        break
                else:
                    if moveVal < bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal
                    beta = min(beta, bestVal)  # Update beta based on bestVal
                    if beta <= alpha:
                        break
    return bestMove

def print_board(board):
    for row in board:
        print(" ".join(row))

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

def is_full(board):
    return all(cell != "_" for row in board for cell in row)

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

def play_game():
    board = [["_"] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    is_maximizer_turn = True
    alpha=float('-inf')
    beta=float("inf")
    while True:
        if is_maximizer_turn:
            print("Maximizer's turn (AI):")
            row, col = findBestMove(board, True,alpha,beta)  # True indicates maximizing player
            symbol = "X"  # Symbol for the maximizing player
        else:
            print("Minimizer's turn (AI):")
            row, col = findBestMove(board, False,alpha,beta)  # False indicates minimizing player
            symbol = "O"  # Symbol for the minimizing player
        board[row][col] = symbol
        print_board(board)
        if is_winner(board, symbol):
            print(f"{symbol} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        is_maximizer_turn = not is_maximizer_turn  # Toggle the turn between maximizer and minimizer

if __name__ == "__main__":
    play_game()


# if __name__ =="__main__":
#     board=[["X","O","X"],
#            ["O","O","X"],
#            ["_","_","_"]
#     ]
    
#     bestMove=findBestMove(board)

#     print("The Optimal Move is :")
#     print("ROW:",bestMove[0]," COL:",bestMove[1])

