class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for src, dst in prerequisites:
            adj[src].append(dst)

        order = []
        visit = set()
        path = set()

        for i in range(numCourses):
            if not self.dfs(i, adj, visit, path, order):
                return []

        return order

    def dfs(self, src, adj, visit, path, order):
        if src in path:
            return False
        if src in visit:
            return True

        path.add(src)
        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, visit, path, order):
                return False
        path.remove(src)
        visit.add(src)
        order.append(src)
        return True