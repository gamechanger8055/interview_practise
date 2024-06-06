'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

import heapq
from collections import Counter
def topKfreqelements(nums,k):
    hp=[]
    mp=Counter(nums)
    for key in mp:
        heapq.heappush(hp,(-mp[key],key))
    l=[]
    while len(l)<k:
        curr=heapq.heappop(hp)
        l.append(curr[1])
    return l

nums = [1,1,1,2,2,3]
k = 2
print(topKfreqelements(nums,k))
