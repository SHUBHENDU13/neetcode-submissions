class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        res = []
        visit = set()
        path = set()

        for i in range(n):
            if not self.dfs(i, adj, visit, path, res):
                return []
        
        res.reverse()
        return res

    def dfs(self, src, adj, visit, path, res):
        if src in path:
            return False
        if src in visit:
            return True

        visit.add(src)
        path.add(src)
        for nei in adj[src]:
            if not self.dfs(nei, adj, visit, path, res):
                return False
        path.remove(src)
        res.append(src)
        return True