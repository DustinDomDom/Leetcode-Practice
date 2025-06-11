'''

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

'''

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

arr_row = []
arr_col = []

def check_row(board, arr_row):
    temp_arr = []

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                temp_arr.append(board[i][j])
        arr_row.append(temp_arr)
        temp_arr = []

    return arr_row


def check_col(board, arr_col):
    temp_arr = []

    for i in range(9):
        for j in range(9):
            if board[j][i] != ".":
                temp_arr.append(board[j][i])
                
        arr_col.append(temp_arr)
        temp_arr = []
        
    return arr_col

print(check_col(board, arr_col))
print(check_row(board, arr_row))

