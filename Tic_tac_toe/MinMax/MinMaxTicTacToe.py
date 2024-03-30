'''
function findBestMove(board):
    bestMove=NULL
    for each move in board:
        if current move is better than bestMove:
            bestMove=currentMove
    return bestMove

'''
'''
function minimax(board,depth,isMaximizingPlayer):
    if current board state is a terminal state:
        return value of the board
    if isMaximizingPlayer:
        bestVal=-INF
        for each move in board:
            value=minimax(board,depth+1,false)
            bestVal=max(bestVal,value)
        return bestVal
    else:
        bestVal=+INF
        for each move in board:
            value=minimax(board,depth+1,true)
            bestVal=min(bestVal,value)
        return bestVal
'''
'''
function isMoveLeft(board):
    for each move in board:
        if current cell is empty:
            return true
    return false
'''
'''
if maximizer has won:
    retunr WIN_SCORE-depth

elif minimizer has won:
    retunr LOOSE_SCORE+depth
'''
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
        
def minimax(board,depth,isMax):
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
                    best=max(best,minimax(board,depth+1,not isMax))

                    # undo move
                    board[i][j]="_"
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
                    best=min(best,minimax(board,depth+1,not isMax))

                    # undo move
                    board[i][j]="_"
        return best
    
# function to return best move for nplayer
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
    while True:
        # Human's turn
        row, col = human_move(board)
        board[row][col] = "X"
        print_board(board)
        if is_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        # AI's turn
        print("AI's turn:")
        row, col = findBestMove(board)
        board[row][col] = "O"
        print_board(board)
        if is_winner(board, "O"):
            print("Sorry, you lose. AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

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

