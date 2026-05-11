# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def bfs(self, root, arr):
        queue = deque()

        if root:
            queue.append(root)

        while(len(queue) > 0):
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            arr.append(temp)
        return arr
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        return self.bfs(root, ans)

        