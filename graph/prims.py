import heapq
def prims_algo(n,adj):
    distance=[float('inf')]*n
    parent=[-1]*n
    mst_set=[False]*n
    priority_queue=[]

    distance[0]=0
    heapq.heappush(priority_queue,(0,0))

    while priority_queue:
        dist,node=heapq.heappop(priority_queue)
        mst_set[node]=True

        for neighbor,weight in adj[node]:
            if not mst_set[neighbor] and weight<distance[neighbor]:
                distance[neighbor]=weight
                parent[neighbor]=node
                heapq.heappush(priority_queue,(weight,neighbor))

    mst=[]
    total_weight=0
    for i in range(1,n):
        if parent[i]!=-1:
            mst.append((parent[i],i,distance[i]))
            total_weight+=distance[i]
    return mst,total_weight


n = 4
adj = [
    [(1, 10), (2, 6), (3, 5)],
    [(0, 10), (3, 15)],
    [(0, 6), (3, 4)],
    [(0, 5), (1, 15), (2, 4)]
]

mst, total_weight = prims_algo(n, adj)
print("Edges in the MST:", mst)
print("Total weight of MST:", total_weight)