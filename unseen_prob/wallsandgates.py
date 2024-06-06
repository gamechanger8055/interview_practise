def wallsAndGates(room):
    m,n=len(room),len(room[0])
    q=[]
    for i in range(m):
        for j in range(n):
            if room[i][j]==0:
                q.append((i,j))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x,y=q.pop(0)
        for p,qu in directions:
            nx,ny=x+p,y+qu
            if 0<=nx<m and 0<=ny<n and room[nx][ny]==INF:
                room[nx][ny]=room[x][y]+1
                q.append((nx,ny))


# Example usage:
INF = 2147483647
grid = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]
wallsAndGates(grid)
for row in grid:
    print(row)
