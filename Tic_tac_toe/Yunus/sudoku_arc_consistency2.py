def is_safe(board, row, col, num):
    # Check if the number is not already present in the row
    if num in board[row]:
        return False
    
    # Check if the number is not already present in the column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if the number is not already present in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    # Enforce arc consistency
    for i in range(9):
        if board[i][col] == num:
            return False
        if board[row][i] == num:
            return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def possible_values(board, row, col):
    values = []
    for i in range(1, 10):
        if is_safe(board, row, col, i):
            values.append(i)
    return values

def forward_tracking(board):
    row, col = find_empty_location(board)
    if row == -1 and col == -1:
        return True
    
    values = possible_values(board, row, col)
    for num in values:
        board[row][col] = num
        if forward_tracking(board):
            return True
        board[row][col] = 0
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku puzzle to solve:")
    print_board(sudoku_board)
    print("\nSolving...\n")
    
    if forward_tracking(sudoku_board):
        print("Sudoku solved:")
        print_board(sudoku_board)
    else:
        print("No solution exists!")