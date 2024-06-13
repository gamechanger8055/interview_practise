'''
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def findMaxDepth(root):
    if not root:
        return 0
    left_height=findMaxDepth(root.left)
    right_height=findMaxDepth(root.right)
    print(left_height,right_height,root.val)
    if left_height==-1 or right_height==-1: #recursively for left and right subtree
        return -1
    if abs(left_height-right_height)>1: #check at any pt if left and right diff >1
        return -1
    return 1+max(left_height,right_height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(findMaxDepth(root))