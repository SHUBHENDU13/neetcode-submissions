class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []

        for src, dst in edges:
            adj[src].append(dst)

        visit = set()
        path = set()
        topSort = []

        def dfs(src, adj, visit, path, topSort):
            if src in visit:
                return True
            if src in path:
                return False

            path.add(src)

            for neighbour in adj[src]:
                if not dfs(neighbour, adj, visit, path, topSort):
                    return False
            path.remove(src)
            visit.add(src)
            topSort.append(src)
            return True
        
        for i in range(n):
            if not i in visit:
                if not dfs(i, adj, visit, path, topSort):
                    return []
        topSort.reverse()
        return topSort
