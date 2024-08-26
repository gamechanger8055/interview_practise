class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n

    def findParent(self,n):
        if self.parent[n]!=n:
            self.parent[n]=self.findParent(self.parent[n])
        return self.parent[n]

    def union(self,u,v):
        parent_u=self.findParent(u)
        parent_v=self.findParent(v)
        if parent_u!=parent_v:
            if self.rank[parent_u]>self.rank[parent_v]:
                self.parent[parent_v]=parent_u
            elif self.rank[parent_u]<self.rank[parent_v]:
                self.parent[parent_u]=parent_v
            else:
                self.parent[parent_u] = parent_v
                self.rank[parent_v]+=1

def kruskals_algo(n, edges):
    edges.sort(key=lambda x:x[2])
    uf=UnionFind(n)
    mst=[]
    total_weight=0
    for u,v,w in edges:
        if uf.findParent(u)!=uf.findParent(v):
            uf.union(u,v)
            mst.append((u,v,w))
            total_weight+=w

    return mst, total_weight


n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, total_weight = kruskals_algo(n, edges)
print("Edges in the MST:", mst)
print("Total weight of MST:", total_weight)

