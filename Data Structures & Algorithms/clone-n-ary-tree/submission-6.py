"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root

        new_root = Node(root.val)
        q = deque([(root, new_root)])

        while q:
            old_node, new_node = q.popleft()

            for child_node in old_node.children:
                new_child_node = Node(child_node.val)
                new_node.children.append(new_child_node)
                q.append((child_node, new_child_node))

        return new_root
        