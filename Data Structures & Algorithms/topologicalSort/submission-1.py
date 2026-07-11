class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []

        for src, dst in edges:
            adj[src].append(dst)

        ts = []
        visit = set()
        path = set()

        for i in range(n):
            if not self.dfs(i, adj, visit, path, ts):
                return []
        ts.reverse()
        return ts

    def dfs(self, src, adj, visit, path, ts):
        if src in visit:
            return True
        if src in path:
            return False

        path.add(src)

        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, visit, path, ts):
                return False
        
        path.remove(src)
        visit.add(src)
        ts.append(src)
        return True