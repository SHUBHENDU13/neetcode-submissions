# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = []
        max_val = root.val
        def dfs(node, max_val):
            max_val = max(max_val, node.val)
            if node.val >= max_val:
                good_nodes.append(node.val)
            if node.left:
                dfs(node.left, max_val)
            if node.right:
                dfs(node.right, max_val)
        dfs(root, -1000)
        return len(good_nodes)
            


            