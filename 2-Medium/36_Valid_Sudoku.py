'''

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

'''

board=[["1","2",".",".","3",".",".",".","."],
       ["4",".",".","5",".",".",".",".","."],
       [".","9","8",".",".",".",".",".","3"],
       ["5",".",".",".","6",".",".",".","4"],
       [".",".",".","8",".","3",".",".","5"],
       ["7",".",".",".","2",".",".",".","6"],
       [".",".",".",".",".",".","2",".","."],
       [".",".",".","4","1","9",".",".","8"],
       [".",".",".",".","8",".",".","7","9"]]



arr_row = []
arr_col = []

def check_row(board, arr_row):
    temp_arr = []

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                temp_arr.append(int(board[i][j]))
        arr_row.append(temp_arr)
        temp_arr = []

    return checker(arr_row)

def checker(arr_check):
    for i in range(len(arr_check)):
        if len(set(arr_check[i])) != len(arr_check[i]):
            return False
        
    return True

def check_col(board, arr_col):
    temp_arr = []

    for i in range(9):
        for j in range(9):
            if board[j][i] != ".":
                temp_arr.append(int(board[j][i]))
                
        arr_col.append(temp_arr)
        temp_arr = []
        
    return checker(arr_col)

print(check_row(board, arr_row),check_col(board, arr_col))


