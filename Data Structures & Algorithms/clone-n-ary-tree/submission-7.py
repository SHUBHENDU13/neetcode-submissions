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

            new_node = Node(node.val)
            for child_node in node.children:
                new_node.children.append(dfs(child_node))

            return new_node

        return dfs(root)