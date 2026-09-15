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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(minheap, [distance, i, j])

        mst = []
        res = 0

        uf = UnionFind(len(points))

        while minheap:
            w, s, d = heapq.heappop(minheap)
            if not uf.union(s, d):
                continue
            mst.append([s, d])
            res += w
        
        return res if len(mst) == len(points) - 1 else -1

        