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
            left, right = max(dfs(root.left), 0), max(dfs(root.right), 0)
            max_sum[0] = max(max_sum[0], root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return max_sum[0]   