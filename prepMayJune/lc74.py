'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''

def combination(candidates,target):
    candidates.sort()
    def backtrack(start,curr_sum,path):
        if curr_sum==target:
            result.append(path[:])
            return
        #main keypoint
        if curr_sum>target:
            return
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtrack(i+1,curr_sum+candidates[i],path)
            path.remove(candidates[i])
        #return
    result=[]
    backtrack(0,0,[])
    return result


candidates = [10,1,2,7,6,1,5]
target = 8
print(combination(candidates,target))