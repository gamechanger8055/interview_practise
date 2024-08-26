'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

def findIfWordExists(board,word):
    m,n=len(board),len(board[0])
    def backtracking(r,c,idx):
        #not safe state
        if idx==len(word):
            return True
        if r<0 or r>=m or c<0 or c>=n or board[r][c]!=word[idx]:
            return False
        temp=board[r][c]
        board[r][c]='$'
        found=backtracking(r-1,c,idx+1) or backtracking(r,c-1,idx+1) or backtracking(r+1,c,idx+1) or backtracking(r,c+1,idx+1)
        board[r][c] = temp
        return found

    for i in range(m):
        for j in range(n):
            if board[i][j]==word[0] and backtracking(i,j,0):
                return True
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(findIfWordExists(board,word))