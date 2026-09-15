class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

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
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minheap = []
        for src, dst, w in edges:
            heapq.heappush(minheap, [w, src, dst])

        uf = UnionFind(n)
        mst = []
        res = 0
        
        while minheap and len(mst) < n - 1:
            w, s, d = heapq.heappop(minheap)
            if not uf.union(s, d):
                continue
            mst.append([s,d])
            res += w
        
        return res if len(mst) == n - 1 else -1
