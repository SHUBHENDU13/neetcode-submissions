class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        visit = set()

        def dfs(src, target):
            if src not in adj or target not in adj:
                return -1.0
            if src == target:
                return 1.0
            visit.add(src)
            for nei, weight in adj[src]:
                if nei not in visit:
                    result = dfs(nei, target)
                    if result != -1.0:
                        visit.remove(src)
                        return weight * result
            visit.remove(src)
            return -1.0

        res = []
        for src, target in queries:
            res.append(dfs(src, target))
        
        return res

            
            