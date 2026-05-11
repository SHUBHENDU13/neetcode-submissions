# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightNodes(self, root, arr):
        queue = deque()

        if root:
            queue.append(root)

        while(len(queue) > 0):
            rightSide = None
            qLen = len(queue)
            for i in range(qLen):
                curr = queue.popleft()
                rightSide = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if rightSide:
                arr.append(rightSide.val)
        return arr

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        return self.rightNodes(root, ans)