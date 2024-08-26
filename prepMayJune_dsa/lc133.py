'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10


Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
'''

def mcm(dp,arr,i,j):
    #base case
    if i>=j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    for k in range(i,j):
        cost=mcm(dp,arr,i,k)+mcm(dp,arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        dp[i][j]=max(dp[i][j],cost)
    return dp[i][j]

def minCostToBurstBallonsMCM(nums):
    arr=[1]+nums+[1]  # considering edge cases
    n=len(arr)
    dp=[[-1 for _ in range(n)] for j in range(n)]
    return mcm(dp,arr,1,n-1)

nums = [3,1,5,8]
print(minCostToBurstBallonsMCM(nums))