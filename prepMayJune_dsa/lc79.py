'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

from collections import deque
def numberOfIslands(grid):
    dirn=[(1,0),(0,1),(-1,0),(0,-1)]
    def safeState(a,b):
        return 0<=a<m and 0<=b<n and grid[a][b]=='1' and (a,b) not in visited

    def bfs(r,c):
        q=deque([(r,c)])
        while q:
            x,y=q.popleft()
            visited.add((x,y))
            for dx,dy in dirn:
                a,b=x+dx,y+dy
                if safeState(a,b):
                    visited.add((a,b))
                    q.append((a,b))
    m,n=len(grid),len(grid[0])
    visited=set()
    island=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1' and (i,j) not in visited:
                bfs(i,j)
                island+=1
    return island

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numberOfIslands(grid))
