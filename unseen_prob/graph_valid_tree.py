from collections import defaultdict

n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
edge=[[0,1], [0,2], [0,3], [1,4]]
def graphValidTree(edges):
    graph=defaultdict(list)
    for a,b in edges:
        if len(graph[b])==1:
            return False
        graph[b].append(a)
    #print(graph)
    return True

print(graphValidTree(edges))