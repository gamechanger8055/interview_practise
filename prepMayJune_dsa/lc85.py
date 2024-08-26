'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.



Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]



Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''

def convertXtoO(board):
    m,n=len(board),len(board[0])
    q=[]
    for i in range(m):
        for j in range(n):
            if i==m-1 or i==0 or j==0 or j==n-1:
                if board[i][j]=='O':
                    board[i][j] = 'Y'
                    q.append((i,j))
    while q:
        x,y=q.pop(0)
        dirn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in dirn:
            a, b = x + dx, y + dy
            if 0<= a < m and 0<= b < n and board[a][b] == 'O':
                board[a][b] = 'Y'
                q.append((a, b))

    for i in range(m):
        for j in range(n):
            if board[i][j]=='O':
                board[i][j] = 'X'
            if board[i][j]=='Y':
                board[i][j] = 'O'





board = [["X","X","O","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]
convertXtoO(board)
print(board)