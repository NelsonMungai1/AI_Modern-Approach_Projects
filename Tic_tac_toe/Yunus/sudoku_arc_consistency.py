import tkinter as tk

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

def solve_sudoku_gui():
    global sudoku_board
    if forward_tracking(sudoku_board):
        update_gui()
    else:
        status_label.config(text="No solution exists!")

def update_gui():
    global sudoku_board
    for i in range(9):
        for j in range(9):
            entry = entries[i][j]
            entry.delete(0, tk.END)
            entry.insert(0, str(sudoku_board[i][j]))
    status_label.config(text="Sudoku solved!")

# Initialize Sudoku board
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

# Create GUI
root = tk.Tk()
root.title("Sudoku Solver")

entries = [[None for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        entry = tk.Entry(root, width=3, font=('Arial', 16))
        entry.grid(row=i, column=j)
        entry.insert(0, str(sudoku_board[i][j]))
        entries[i][j] = entry

solve_button = tk.Button(root, text="Solve Sudoku", command=solve_sudoku_gui)
solve_button.grid(row=9, columnspan=9)

status_label = tk.Label(root, text="")
status_label.grid(row=10, columnspan=9)

root.mainloop()
