"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        def dfs(node):
            if not node:
                return
            new_node = Node()
            new_node.val = node.val

            for child in node.children:
                new_node.children.append(dfs(child))

            return new_node

        return dfs(root)


