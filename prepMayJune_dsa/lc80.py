'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''

from collections import deque
def maxAreaOfIslands(grid):
    dirn=[(1,0),(0,1),(-1,0),(0,-1)]
    def safeState(a,b):
        return 0<=a<m and 0<=b<n and grid[a][b]==1 and (a,b) not in visited

    def bfs(r,c):
        q=deque([(r,c)])
        islands=1
        while q:
            x,y=q.popleft()
            visited.add((x,y))
            for dx,dy in dirn:
                a,b=x+dx,y+dy
                if safeState(a,b):
                    islands+=1
                    visited.add((a,b))
                    q.append((a,b))
        return islands

    m,n=len(grid),len(grid[0])
    visited=set()
    maxIsland=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1 and (i,j) not in visited:
                islands=bfs(i,j)
                maxIsland=max(maxIsland,islands)
    return maxIsland

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIslands(grid))