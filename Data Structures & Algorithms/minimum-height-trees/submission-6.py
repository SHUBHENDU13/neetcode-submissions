class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def bfs(start):
            parent = {start: None}
            q = deque([start])
            last = start
            while q:
                node = q.popleft()
                last = node
                for nei in adj[node]:
                    if nei not in parent:
                        parent[nei] = node
                        q.append(nei)

            return last, parent

        a, _ = bfs(0) # find one end of longest path
        b, parent = bfs(a) # find other end on of longest path with path itself

        node = b
        path = []
        while node is not None:
            path.append(node)
            node = parent[node]

        res = []
        length = len(path)
        if length % 2 == 0:
            res.append(path[length//2 - 1])
            res.append(path[length//2])
        else:
            res.append(path[length//2])

        return res


        