# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        forward = [True]
        res = []
        while q:
            # gather each node at a level
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # reverse the level based on whether previous level for forward
            if not forward[0]:
                level.reverse()
            # append to result
            res.append(level)
            
            forward[0] = True if not forward[0] else False
        
        return res
        
            
