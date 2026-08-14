# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def findDiameter(root):
            if not root:
                return 0
            leftH = findDiameter(root.left)
            rightH = findDiameter(root.right)
            diameter[0] = max(diameter[0], leftH + rightH)
            return 1 + max(leftH, rightH)
        findDiameter(root)
        return diameter[0]