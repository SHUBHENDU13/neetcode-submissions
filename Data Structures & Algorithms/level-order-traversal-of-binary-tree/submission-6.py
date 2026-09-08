# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []

        q = deque()
        q.append(root)
        while q:
            tmp = []
            for _ in range(len(q)):
                pop = q.popleft()
                tmp.append(pop.val)
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            ans.append(tmp)
        return ans
            