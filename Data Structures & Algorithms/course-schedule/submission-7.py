class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for src, dst in prerequisites:
            adj[src].append(dst)

        visit = set()
        path = set()

        for i in range(numCourses):
            if not self.dfs(i, adj, visit, path):
                return False

        return True

    def dfs(self, src, adj, visit, path):
        if src in visit:
            return True
        if src in path:
            return False

        path.add(src)
        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, visit, path):
                return False
        path.remove(src)
        visit.add(src)
        return True