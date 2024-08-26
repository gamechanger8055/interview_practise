'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''
def findMinInRotatedSortedArray(nums):
    n=len(nums)
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<nums[(mid+1)%n] and nums[mid]<nums[(mid-1+n)%n]:
            return mid
        elif nums[mid]>nums[0]:
            left+=1
        else:
            right-=1
    return -1

def binary_search(nums,target):
    left,right=0,len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left+=1
        else:
            right-=1
    return -1

def SearchInRotatedSortedArray(nums,target):
    min_index=findMinInRotatedSortedArray(nums)
    first_half=binary_search(nums[:min_index],target)
    second_half=binary_search(nums[min_index:],target)
    if first_half==-1 and second_half==-1:
        return -1
    return first_half if first_half!=-1 else second_half+min_index

nums = [4,5,6,7,0,1,2]
target = 1
print(SearchInRotatedSortedArray(nums,target))



