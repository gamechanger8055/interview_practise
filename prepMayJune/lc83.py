'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''

def rottingOranges(grid):
    m, n = len(grid), len(grid[0])
    dirn = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = []
    max_time=0
    fresh_oranges=0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh_oranges+=1
            if grid[i][j] == 2:
                q.append((i, j, 0))
    while q:
        x, y, time = q.pop(0)
        for a, b in dirn:
            dx, dy = x + a, y + b
            if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:  # and (dx,dy) not in visited:
                grid[dx][dy] = 2
                fresh_oranges-=1
                q.append((dx, dy, time + 1))
                max_time=max(max_time,time+1)
    return max_time if fresh_oranges==0 else -1

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(rottingOranges(grid))
#print(grid)