import random 
possible_numbers=[1,2,3,4,5,6,7,8,9]
print("WWelcome to tic tac toe")
print("--------------------------")
game_board=[[1,2,3],
             [4,5,6],
             [7,8,9]]

rows=3
cols=3
# function to print the gameboard
def print_board():
    for i in range(rows):
        print("\n+---+---+---+")
        print("|",end="")
        for j in range(cols):
            print("",game_board[i][j],end=" |")
    print("\n+---+---+---+")

# modify the array_board
def modify_board(num,turn):
    num-=1
    if(num==0):
        game_board[0][0]=turn
    elif(num==1):
        game_board[0][1]=turn
    elif(num==2):
        game_board[0][2]=turn
    elif(num==3):
        game_board[1][0]=turn
    elif(num==4):
        game_board[1][1]=turn
    elif(num==5):
        game_board[1][2]=turn
    elif(num==6):
        game_board[2][0]=turn
    elif(num==7):
        game_board[2][1]=turn 
    elif(num==8):
        game_board[2][2]=turn 

def check_winner(gameBoard):
    # x axis
    if(gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O'):
        print("O has won!")
        return "O"
    #y-axis
    if(gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
        print("O has won!")
        return "O"
    #diagonal
    elif(gameBoard[0][0]=="X" and gameBoard[1][1]=="X" and gameBoard[2][2]=="X"):
        print("X has Won")
        return "X"
    elif(gameBoard[0][2]=="X" and gameBoard[1][1]=="X" and gameBoard[2][0]=="X"):
        print("X has Won")
        return "X"
    elif(gameBoard[0][0]=="O" and gameBoard[1][1]=="O" and gameBoard[2][2]=="O"):
        print("O has Won")
        return "O"
    elif(gameBoard[0][2]=="O" and gameBoard[1][1]=="O" and gameBoard[2][0]=="O"):
        print("O has Won")
        return "O"
    else:
        return "N"

leave_loop=False
turnCounter=0

while(leave_loop==False):
    
    
    if(turnCounter%2==1):
        print_board()
        number_picked=int(input("\n Choose a number [1-9]:"))
        if (number_picked>=1 and number_picked<=9):
            modify_board(number_picked,"X")
            possible_numbers.remove(number_picked)
        else:
            print("You picked a wrong number try again")
        turnCounter+=1
        # computers turn 
    else:
        while(True):
            cpuChoice=random.choice(possible_numbers)
            print("\n Cpu Choice: ",cpuChoice)
            if (cpuChoice in possible_numbers):
                modify_board(cpuChoice,"O")
                possible_numbers.remove(cpuChoice)
                turnCounter+=1
                break

    winner = check_winner(game_board)
    if(winner != "N"):
        print("\nGame over! Thank you for playing :)")
        break
    




