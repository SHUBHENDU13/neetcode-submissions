# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorder_helper(self, root, ans):
        stack = [root]
        visited = [False]

        while stack:
            curr, visit = stack.pop(), visited.pop()
            if curr:
                if visit:
                    ans.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.postorder_helper(root, ans)
        return ans