class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.num_components = n

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        self.num_components -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,e in enumerate(edges):
            e.append(i)

        edges.sort(key=lambda e: e[2])

        uf = UnionFind(n)
        mst_weight = 0
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w
        
        critical, pseudo = [], []

        for n1, n2, e_weight, i in edges:
            # try without current edge
            uf = UnionFind(n)
            weight = 0
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
            if uf.num_components > 1 or weight > mst_weight:
                critical.append(i)
                continue

            # try with current edge
            uf = UnionFind(n)
            weight = e_weight
            uf.union(n1, n2)
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]
        



        