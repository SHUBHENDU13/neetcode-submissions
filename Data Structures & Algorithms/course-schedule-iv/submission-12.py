class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for dst, src in prerequisites:
            adj[src].append(dst)

        visit = set()
        cache = {}
        res = []

        def dfs(crs, target):
            if crs in visit:
                return False
            if crs == target:
                return True
            if (crs, target) in cache:
                return cache[(crs, target)]

            visit.add(crs)
            tmp = False
            for nei in adj[crs]:
                if dfs(nei, target):
                    tmp = True
                    break
            visit.remove(crs)
            cache[(crs, target)] = tmp
            return cache[(crs, target)]

        for target, crs in queries:
            res.append(dfs(crs, target))
        
        return res