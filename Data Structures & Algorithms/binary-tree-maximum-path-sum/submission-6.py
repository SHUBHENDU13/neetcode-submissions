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
            # we check if returned sum for the node is -ve, if yes, 
            # no point including that node as we want to maximise the sum(greedy) 
            # and we skip that hence returning 0
            left, right = max(dfs(root.left), 0), max(dfs(root.right), 0)
            max_sum[0] = max(max_sum[0], root.val + left + right)
            # return root.val + max of either as we can include only one path and not both
            return root.val + max(left, right)

        dfs(root)
        return max_sum[0]   