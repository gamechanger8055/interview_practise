'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''

def wallsAndGates(grid):
    m,n=len(grid),len(grid[0])
    dirn = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q=[]
    for i in range(m):
        for j in range(n):
            if grid[i][j]==0:
                q.append((i,j,0))
    visited=set()
    while q:
        x,y,dist=q.pop(0)
        visited.add((x,y))
        for a,b in dirn:
            dx,dy=x+a,y+b
            if 0<=dx<m and 0<=dy<n and grid[dx][dy]==INF:# and (dx,dy) not in visited:
                grid[dx][dy]=dist+1
                q.append((dx,dy,dist+1))

INF = 2147483647
grid = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]
wallsAndGates(grid)
print(grid)