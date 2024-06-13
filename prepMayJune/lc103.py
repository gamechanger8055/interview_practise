'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements
 in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''

def partitionEqualSumSubsets(nums):
    if not nums or sum(nums)%2!=0:
        return False
    target=sum(nums)//2
    dp=[[False for i in range(target+1)] for j in range(len(nums)+1)]
    for i in range(len(nums)+1):
        dp[i][0]=True
    for i in range(1,len(nums)+1):
        for j in range(1,target+1):
            if nums[i-1]<=j:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]

nums = [1,5,11,5]
print(partitionEqualSumSubsets(nums))



#using 1 d dp
def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    dp = [False] * (target_sum + 1)
    dp[0] = True

    for num in nums:
        for j in range(target_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target_sum]


# Example usage:
nums1 = [1, 5, 11, 5]
print(canPartition(nums1))  # Output: True

nums2 = [1, 2, 3, 5]
print(canPartition(nums2))  # Output: False
