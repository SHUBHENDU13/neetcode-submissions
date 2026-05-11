# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSumHelper(self, root, ps, ts):
        if not root:
            return False

        ps += root.val

        if not root.left and not root.right and ps == ts:
            return True

        if self.pathSumHelper(root.left, ps, ts):
            return True

        if self.pathSumHelper(root.right, ps, ts):
            return True

        ps -= root.val
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = 0
        return self.pathSumHelper(root, pathSum, targetSum)

