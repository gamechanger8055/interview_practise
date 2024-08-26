'''
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

def maxProductSubarray(nums):
    mx=mn=nums[0]
    max_product=0
    for i in range(1,len(nums)):
        temp=mx
        mx=max(nums[i],mx*nums[i],mn*nums[i])
        mn=min(nums[i],temp*nums[i],mn*nums[i])
        max_product=max(max_product,mx)
    return max_product

nums = [2,3,-2,4]
print(maxProductSubarray(nums))