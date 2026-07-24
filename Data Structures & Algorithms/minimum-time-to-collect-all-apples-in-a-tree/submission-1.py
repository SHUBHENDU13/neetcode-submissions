class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visit = set()
        def dfs(node):
            time = 0
            visit.add(node)
            for child in adj[node]:
                if child in visit:
                    continue
                childTime = dfs(child)
                if childTime or hasApple[child]:
                    time += 2 + childTime

            return time

        return dfs(0)