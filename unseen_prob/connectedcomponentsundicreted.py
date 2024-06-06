from collections import defaultdict
n = 5
edges = [[0, 1], [1, 2], [3, 4]]

edge = [[0, 1], [1, 2], [2, 3], [3, 4]]
def connectedComponentsInUndirectedGraoh(n,edges):
    graph=defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited=set()
    def bfs(src):
        q=[src]
        visited.add(src)
        while q:
            curr=q.pop(0)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
    count=0
    for i in range(n):
        if i not in visited:
            bfs(i)
            count+=1
    return count

print(connectedComponentsInUndirectedGraoh(n,edge))



