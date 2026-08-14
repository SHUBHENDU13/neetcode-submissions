# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = [0]
        def findMaxDepth(root):
            if not root:
                return 0
            cur_depth = 1 + max(findMaxDepth(root.left), findMaxDepth(root.right))
            max_depth[0] = max(max_depth[0], cur_depth)
            return cur_depth

        findMaxDepth(root)
        return max_depth[0]