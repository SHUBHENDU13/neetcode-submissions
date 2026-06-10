class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.num_components = n

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        self.num_components -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i in range(len(edges)):
            uf.union(edges[i][0], edges[i][1])

        return uf.num_components
        