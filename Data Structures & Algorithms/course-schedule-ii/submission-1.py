class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()
        path = set()

        res = []

        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True

            visit.add(crs)
            path.add(crs)
            for nei in adj[crs]:
                if not dfs(nei): return False
            path.remove(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i): return []

        return res