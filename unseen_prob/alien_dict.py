from collections import defaultdict

N = 5
K = 4
dict = ["baa","abcd","abca","cab","cad"]

def topSort(n,k,dict):
    indegree=[0 for i in range(k)]
    graph=defaultdict(list)
    for i in range(n-1):
        word1=dict[i]
        word2=dict[i+1]
        for j in range(min(len(word1),len(word2))):
            if word1[j]!=word2[j]:
                graph[word1[j]].append(word2[j])
                indegree[ord(word2[j])-ord('a')]+=1
                break
    #print(graph,indegree)
    ans=[]
    q=[chr(i+97) for i in range(k) if indegree[i]==0]
    while q:
        curr=q.pop(0)
        ans.append(curr)
        for node in graph[curr]:
            indegree[ord(node)-ord('a')]-=1
            if indegree[ord(node)-ord('a')]==0:
                q.append(node)
    return ans


print(topSort(N,K,dict))

