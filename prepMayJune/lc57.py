'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def constructBinaryTreeFromInorderAndPostOrder(inorder,postorder):
    if not inorder or not postorder:
        return
    root_val = postorder.pop()
    index = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left = constructBinaryTreeFromInorderAndPreOrder(inorder[:index], postorder[:index])
    root.right = constructBinaryTreeFromInorderAndPreOrder(inorder[index + 1:], postorder[index:])
    return root


def constructBinaryTreeFromInorderAndPreOrder(inorder,preorder):
    if not inorder or not preorder:
        return
    root_val = preorder.pop(0)
    index = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left =constructBinaryTreeFromInorderAndPreOrder(inorder[:index],preorder)
    root.right=constructBinaryTreeFromInorderAndPreOrder(inorder[index+1:],preorder)
    return root

def inOrderRecursive(root):
    if not root:
        return
    print("inorder",root.val)
    inOrderRecursive(root.left)
    inOrderRecursive(root.right)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
postorder=[9,15,7,20,3]
root=constructBinaryTreeFromInorderAndPostOrder(inorder,postorder)
inOrderRecursive(root)
root1=constructBinaryTreeFromInorderAndPreOrder(inorder,preorder)
inOrderRecursive(root1)

