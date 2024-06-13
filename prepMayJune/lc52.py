'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

def inOrderRecursive(root):
    if not root:
        return
    print(root.val)
    inOrderRecursive(root.left)
    inOrderRecursive(root.right)
def preOrderRecursive(root):
    if not root:
        return
    preOrderRecursive(root.left)
    print(root.val)
    preOrderRecursive(root.right)
def postOrderRecursive(root):
    if not root:
        return
    postOrderRecursive(root.left)
    postOrderRecursive(root.right)
    print(root.val)
def inOrderIterative(root):
    stack=[]
    curr=root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr=curr.left
        curr=stack.pop()
        print(curr.val)
        curr=curr.right

def preOrderIterative(root):
    stack=[root]
    while stack:
        curr=stack.pop()
        print("preorder",curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

def postOrderIterative(root):
    stack1,stack2=[root],[]
    while stack1:
        curr=stack1.pop()
        stack2.append(curr.val)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    print(stack2[::-1])
def levelOrderIterative(root):
    q=[root]
    while q:
        curr=q.pop(0)
        print("Level order",curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

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

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

inOrderRecursive(root)
print()
preOrderRecursive(root)
print()
postOrderRecursive(root)
print()
inOrderIterative(root)
print()
preOrderIterative(root)
print()
postOrderIterative(root)
print()
levelOrderIterative(root)

