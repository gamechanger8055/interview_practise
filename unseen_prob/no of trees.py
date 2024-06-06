'''
1. All The BST
Medium
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

2
Input
1 2
2 1
Output
Explaination:

The possible BSTs having 2 nodes and values 1 to 2 are :-
      1           2
     /      &       \
   2                  1
Constraints:

1 <= n <= 8
Input Format:

Given an integer representing number of required nodes.

Output Format:

Return a vector containing root nodes of structurally unique BST's with n nodes.


'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # write your code here
        def generateTree(start, end):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end + 1):
                left_subtree = generateTree(start, i - 1)
                right_subtree = generateTree(i + 1, end)
                for left in left_subtree:
                    for right in right_subtree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees

        if n == 0:
            return []
        return generateTree(1, n)
