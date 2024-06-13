'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
'''

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def removeNthNodeFromEndOfLinkedList(head,n):
    dummy=ListNode()
    dummy.next=head
    first=second=dummy
    for i in range(n+1):
        first=first.next
    while first:
        first=first.next
        second=second.next
    second.next=second.next.next
    return dummy.next

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#print(findMiddle(head).val)
new_head=removeNthNodeFromEndOfLinkedList(head,2)
printLinkedList(new_head)

