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

def check_row(board,temp):
    for each_row in range(0,9):

        validate = len(list(map(int,temp.join(board[each_row]).replace('.',"")))) == len(list(set(map(int,temp.join(board[each_row]).replace('.',"")))))
    
    return validate == True

def check_col(board):
    validate = list(zip(*board))

    validate = [
        [x for x in col if x != '.']
        for col in validate
    ]

    for col in validate:
        if len(col) != len(set(col)):
            return False

    return True

def valid(board):
        
