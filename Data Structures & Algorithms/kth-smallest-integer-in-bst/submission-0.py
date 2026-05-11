# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root, arr):
        if not root:
            return []

        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right, arr)
        return arr

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArr = []
        sortedArr = self.dfs(root, sortedArr)
        return sortedArr[k-1]