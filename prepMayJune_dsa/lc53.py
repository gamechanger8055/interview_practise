'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

from collections import OrderedDict
def topView(root):
    q = [(root, 0)]
    mp = {}
    while q:
        curr, horizontal_distance = q.pop(0)
        if horizontal_distance not in mp:
            mp[horizontal_distance] = curr.val
        if curr.left:
            q.append((curr.left, horizontal_distance - 1))
        if curr.right:
            q.append((curr.right, horizontal_distance + 1))
    return [mp[hd] for hd in sorted(mp)]


def bottomView(root):
    q = [(root,0)]
    mp={}
    while q:
        curr,horizontal_distance = q.pop(0)
        mp[horizontal_distance]=curr.val
        if curr.left:
            q.append((curr.left,horizontal_distance-1))
        if curr.right:
            q.append((curr.right,horizontal_distance+1))
    #print(mp)
    return [mp[hd] for hd in sorted(mp)]

def leftView(root):
    q = [root]
    while q:
        for i in range(len(q)):
            curr = q.pop(0)
            if i==0:
                print("left view", curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

def rightView(root):
    q = [root]
    while q:
        level=len(q)
        for i in range(len(q)):
            curr = q.pop(0)
            if i==level-1:
                print(curr.val)
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

print(topView(root))
print()
print(bottomView(root))
print()
leftView(root)
print()
rightView(root)
