'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
'''

def kthSmallest(root,k):
    curr=root
    stack=[]
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left
        curr=stack.pop()
        k-=1
        if k==0:
            return curr.val
        curr=curr.right
    return -1

def kthLargest(root,k):
    curr = root
    stack = []
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.left
    return -1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example Tree
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
print(kthSmallest(root,2))
print(kthLargest(root,2))

