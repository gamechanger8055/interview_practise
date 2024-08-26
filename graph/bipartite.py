from collections import defaultdict,deque

def bipartite_dislikes(n,dislikes):
    graph=defaultdict(list)
    for a,b in dislikes:
        graph[a].append(b)
        graph[b].append(a)

    color=[0]*(n+1)

    def bfs(start):
        q=deque([start])
        color[start]=1
        while q:
            node=q.popleft()
            for neighbors in graph[node]:
                if color[neighbors]==0:
                    color[neighbors]=-color[node]
                    q.append(neighbors)
                elif color[neighbors]==color[node]:
                    return False
        return True

    for i in range(1,n+1):
        print(color)
        if color[i]==0:
            if not bfs(i):
                return False
    return True

N = 4
dislikes = [[1,2], [1,3],[2,4]]
print(bipartite_dislikes(N,dislikes))




