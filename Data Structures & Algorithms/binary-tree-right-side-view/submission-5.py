# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # store every level values in list of list and return a list of every internal list's last element
        # [[1],[2,3],[4,5]] -> [1,3,5]

        q = deque()
        arr = []
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                arr.append(level)

        res = []
        for i in range(len(arr)):
            res.append(arr[i][-1])
        
        return res


