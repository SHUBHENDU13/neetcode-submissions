# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#'
        serialized = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                serialized.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                serialized.append('#')
        return ','.join(serialized)
        
    # Decodes your encoded data to tree.
    # 1,2,3,#,#,4,5,#,#,#,#
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == '#':
            return None

        nodes = data.split(',')
        root = TreeNode(int(data[0]))
        q = deque()
        q.append(root)
        i = 1
        while q and i < len(nodes):
            node = q.popleft()

            # left child
            if nodes[i] != '#':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1

            # right child
            if nodes[i] != '#':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        
        return root

            


    


