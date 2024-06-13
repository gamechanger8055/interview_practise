'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''

from collections import defaultdict

def canFinishAllCourses(prerequisites, numCourses):
    indegree=[0]*numCourses
    graph=defaultdict(list)
    for a,b in prerequisites:
        graph[b].append(a)
        indegree[a]+=1
    q=[]
    for i in range(numCourses):
        if indegree[i]==0:
            q.append(i)
    visited=set()
    while q:
        curr=q.pop(0)
        visited.add(curr)
        for neighbor in graph[curr]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0 and neighbor not in visited:
                q.append(neighbor)
    return len(visited)==numCourses

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinishAllCourses(prerequisites,numCourses))
