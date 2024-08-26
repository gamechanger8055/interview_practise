'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''


'''
s1-s2==target
s1+s2=sum
'''

def findWaysToTargetSum(nums,target):
    sm=sum(nums)
    if (target+sm)%2!=0:
        return 0
    diff=(target+sm)//2
    dp=[[0 for i in range(diff+1)] for j in range(len(nums)+1)]
    for j in range(len(nums)+1):
        dp[j][0]=1

    for i in range(1,len(nums) + 1):
        for j in range(1,diff + 1):
            if nums[i-1]<=j:
                dp[i][j]=dp[i-1][j-nums[i-1]]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[len(nums)][diff]

nums = [1,1,1,1,1]
target = 3
print(findWaysToTargetSum(nums,target))