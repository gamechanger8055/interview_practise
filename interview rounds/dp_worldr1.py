
'''

[15:18] Sai Kumar Reddy

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.

Each column must contain the digits 1-9 without repetition.

Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.

Only the filled cells need to be validated according to the mentioned rules.


Input: board = 

[["5","3",".",".","7",".",".",".","."]

,["6",".",".","1","9","5",".",".","."]

,[".","9","8",".",".",".",".","6","."]

,["8",".",".",".","6",".",".",".","3"]

,["4",".",".","8",".","3",".",".","1"]

,["7",".",".",".","2",".",".",".","6"]

,[".","6",".",".",".",".","2","8","."]

,[".",".",".","4","1","9",".",".","5"]

,[".",".",".",".","8",".",".","7","9"]]

Output: true


'''


def validSoduku(board):
    res = []

    for i in range(9):

        for j in range(9):

            element = board[i][j]

            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]

    return len(res) == len(set(res))


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]

    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]

    , [".", "9", "8", ".", ".", ".", ".", "6", "."]

    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]

    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]

    , ["7", ".", ".", ".", "2", "6", ".", ".", "6"]

    , [".", "6", ".", ".", ".", ".", "2", "8", "."]

    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]

    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board1 = [["8", "3", ".", ".", "7", ".", ".", ".", "."]

    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]

    , [".", "9", "8", ".", ".", ".", ".", "6", "."]

    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]

    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]

    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]

    , [".", "6", ".", ".", ".", ".", "2", "8", "."]

    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]

    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(validSoduku(board1))


'''

Given an integer n, return the nth digit of the infinite integer sequence 

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

Example 1:

Input: n = 3 Output: 3

Example 2:

Input: n = 11 Output: 0

Explanation: 

The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

'''


def nthDigit(n):
    dl, cnt = 1, 9

    while n > dl * cnt:
        n -= (dl * cnt)

        dl += 1

        cnt += 10

    start = 10 ** (dl - 1)

    num = start + (n - 1) // dl

    digit = (n - 1) % dl

    return int(str(num)[digit])


n = 200

print(nthDigit(n))

