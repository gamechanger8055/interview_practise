'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def merge2SortedLists(l1,l2):
    dummy = ListNode()
    temp = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    while l1:
        temp.next = l1
        temp = temp.next
        l1 = l1.next
    while l2:
        temp.next = l2
        temp = temp.next
        l2 = l2.next
    return dummy.next



