'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
'''

import heapq
def kthSmallest(nums,k):
    hp=[]
    for num in nums:
        if len(hp)==k:
            heapq.heappushpop(hp,-num)
        else:
            heapq.heappush(hp,-num)
    return -heapq.heappop(hp)
def kthLargest(nums,k):
    hp = []
    for num in nums:
        if len(hp) == k:
            heapq.heappushpop(hp, num)
        else:
            heapq.heappush(hp, num)
    return heapq.heappop(hp)

class KthLargest:
    def __init__(self,k,nums):
        self.k=k
        self.hp=nums
        heapq.heapify(self.hp)
    def add(self,val):
        heapq.heappush(self.hp, val)
        while len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]

nums=[1,7,3,8,2]
k=2
print(kthSmallest(nums,k))
print(kthLargest(nums,k))

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))#   // return 4
print(kthLargest.add(5))#;   // return 5
print(kthLargest.add(10))#;  // return 5
print(kthLargest.add(9))#;   // return 8
print(kthLargest.add(4))#;   // return 8
