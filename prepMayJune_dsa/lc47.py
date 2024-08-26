'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

'''


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def createBinaryTree(vals, index=0):
    if index < len(vals):
        value = vals[index]
        if value is None:
            return None
        node = TreeNode(value)
        node.left = createBinaryTree(vals, 2 * index + 1)
        node.right = createBinaryTree(vals, 2 * index + 2)
        return node
    return None

def findMaxDepth(root):
    if not root:
        return 0
    left_height=findMaxDepth(root.left)
    right_height=findMaxDepth(root.right)
    return 1+max(left_height,right_height)
def maxDiameterOfBinaryTree(root):
    if not root:
        return 0
    left_height=findMaxDepth(root.left)
    right_height=findMaxDepth(root.right)
    left_diameter=maxDiameterOfBinaryTree(root.left)
    right_diameter=maxDiameterOfBinaryTree(root.right)
    return max(1+left_height+right_height,left_diameter,right_diameter)


# Example usage
# values = [1, 2, 3, 4, 5]
# root = createBinaryTree(values)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Diameter of the binary tree:", maxDiameterOfBinaryTree(root))