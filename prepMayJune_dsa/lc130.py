'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''


def longestIncreasingPathInMatrix(matrix):
    m,n=len(matrix),len(matrix[0])
    dp={}
    def dfs(r,c,prevVal):
        if r<0 or r==m or c<0 or c==n or matrix[r][c]<=prevVal:
            return 0
        if (r,c) in dp:
            return dp[(r,c)]
        result=1
        result=max(result,1+dfs(r+1,c,matrix[r][c]))
        result = max(result, 1+dfs(r, c+1, matrix[r][c]))
        result = max(result,1+ dfs(r-1, c, matrix[r][c]))
        result = max(result, 1+dfs(r, c-1, matrix[r][c]))
        dp[(r,c)]=result
        return result

    for i in range(m):
        for j in range(n):
            dfs(i,j,-1)
    return max(dp.values())

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPathInMatrix(matrix))