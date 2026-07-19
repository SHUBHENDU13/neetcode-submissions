# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            # current depth is 1 since node is not null
            depth = 1
            leftH = dfs(node.left) # depth of left subtree
            rightH = dfs(node.right) # depth of right subtree
            depth = max(depth + leftH, depth + rightH)
            return depth
        
        return dfs(root)




            