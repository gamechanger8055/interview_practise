'''
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def reverseLinkedListRecursive(head):
    if not head or not head.next:
        return head
    new_head=reverseLinkedListRecursive(head.next)
    head.next.next=head
    head.next=None
    return new_head
def reverseLinkedListIterative(head):
    if not head or not head.next:
        return head
    prev=None
    curr=head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev


def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original list:")
printLinkedList(head)

reversed_head = reverseLinkedListRecursive(head)
print("Reversed list:")
printLinkedList(reversed_head)

reversed_head = reverseLinkedListIterative(head)
print("Reversed list Iterative:")
printLinkedList(reversed_head)