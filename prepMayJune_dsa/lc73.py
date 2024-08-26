'''
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''

def subsets(nums):
    def backtrack(start,path):
        result.append(path[:])
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i+1,path)
            path.remove(nums[i])
    result=[]
    backtrack(0,[])
    return result

print(subsets([1,2,2]))