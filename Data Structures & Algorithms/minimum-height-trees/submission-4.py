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

        a, _ = bfs(0)
        b, parent = bfs(a)

        path = []
        node = b

        while node is not None:
            path.append(node)
            node = parent[node]

        res = []
        if len(path) % 2 == 0:
            res.append(path[len(path)//2 - 1])
            res.append(path[len(path)//2])
        else:
            res.append(path[len(path)//2])

        return res