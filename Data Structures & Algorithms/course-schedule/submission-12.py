class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        cache = {}

        # visit = set()
        path = set()

        def dfs(crs):
            if crs in path:
                return False
            if crs in cache:
                return cache[crs]
            # if crs in visit:
            #     return True

            # visit.add(crs)
            path.add(crs)
            tmp = True
            for nei in adj[crs]:
                if not dfs(nei):
                    tmp = False
                    break
            path.remove(crs)
            cache[crs] = tmp
            return cache[crs]

        for i in range(numCourses):
            if not dfs(i): return False
        return True
        