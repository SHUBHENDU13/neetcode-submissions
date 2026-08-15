# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [root.val]
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            max_sum[0] = max(max_sum[0], root.val + left + right)
            if root.val + left + right < 0:
                return 0
            else:
                return max(root.val + left, root.val + right)
        dfs(root)
        return max_sum[0]   