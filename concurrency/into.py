# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(node):
            nonlocal res
            if not node: return True, inf, -inf, 0
            left_valid, left_min, left_max, left_sum = recur(node.left)
            right_valid, right_min, right_max, right_sum = recur(node.right)
            if left_valid and right_valid and left_max < node.val < right_min: res = max(res, left_valid+right_sum+node.val)
            return left_valid and right_valid and left_max < node.val < right_min, min(left_min, right_min, node.val), 
            max(left_max, right_max, node.val), left_valid+right_sum+node.val
        recur(root)
        return res