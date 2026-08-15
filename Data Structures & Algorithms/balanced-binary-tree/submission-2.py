# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            leftH = dfs(root.left)
            rightH = dfs(root.right)
            balanced = (leftH[0] and rightH[0] and abs(leftH[1] - rightH[1]) <= 1)
            return [balanced, 1 + max(leftH[1], rightH[1])]
        return dfs(root)[0]
