'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def reverseList(head):
    prev=None
    curr=head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev

def findMiddle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
def reorderList(head):
    middle=findMiddle(head)
    reversedHead=reverseList(middle.next)
    middle.next=None
    first_half_head,second_half_head=head,reversedHead
    while second_half_head:
        temp1,temp2=first_half_head.next,second_half_head.next
        first_half_head.next=second_half_head
        second_half_head.next=temp1
        first_half_head,second_half_head=temp1,temp2
    return head


def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#print(findMiddle(head).val)
new_head=reorderList(head)
printLinkedList(new_head)
