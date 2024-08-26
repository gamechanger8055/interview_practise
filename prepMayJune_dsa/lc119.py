'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18


Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.

'''

# -------------------   kruskal algorithm ------------------------------------------

class UnionFind:
    def __init__(self,n):
        self.rank=[0]*n
        self.parent=list(range(n))

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        parent_x=self.find(x)
        parent_y=self.find(y)
        if parent_x==parent_y:
            return False
        else:
            if parent_x<parent_y:
                self.parent[parent_x]=parent_y
            elif parent_x<parent_y:
                self.parent[parent_y] = parent_x
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x]+=1
        return True

def manhattan_distance(point1,point2):
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
def minCostToConnectAllPoints(points):
    n=len(points)
    edges=[]
    for i  in range(n):
        for j in range(i+1,n):
            edges.append((manhattan_distance(points[i],points[j]),i,j))
    edges.sort(key=lambda x:x[0])

    uf=UnionFind(n)
    min_cost=0
    edges_added=0
    for edge in edges:
        cost,u,v=edge
        print(u,v,cost)
        if uf.union(u,v):
            min_cost+=cost
            edges_added+=1
        if edges_added==n-1:
            return min_cost


print(minCostToConnectAllPoints(points=[[0,0],[2,2],[3,10],[5,2],[7,0]]))