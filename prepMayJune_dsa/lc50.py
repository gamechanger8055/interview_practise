'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''

def checkSameTree(p,q):
    if not p and not q:
        return True
    return (p and q) and (p.val==q.val) and checkSameTree(p.left,q.left) and checkSameTree(p.right,q.right)
def isSubTree(root,subroot):
    if not root:
        return False
    if checkSameTree(root,subroot):
        return True
    return checkSameTree(root.left,subroot) or checkSameTree(root.right,subroot)
