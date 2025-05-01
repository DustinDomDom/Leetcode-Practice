'''

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

'''

str = 'PAYPALISHIRING'
NumRows = 3
ret = ""

def convert(str, rows):

    if NumRows == 1:
        return str

    ret = ""

    for i in range(rows):
        if i % 2 == 0: ret += str[i::rows+1]
        else : ret += str[i::rows-1]

    return ret

print(convert(str, NumRows))








