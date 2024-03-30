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
        return score
    
    # if minimizer has won game returns his/her evaluated score
    if(score==-10):
        return score
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

    print("The value of the best Move is :",bestVal)
    print()
    return bestMove

if __name__ =="__main__":
    board=[["X","O","X"],
           ["O","O","X"],
           ["_","_","_"]
    ]
    
    bestMove=findBestMove(board)

    print("The Optimal Move is :")
    print("ROW:",bestMove[0]," COL:",bestMove[1])

