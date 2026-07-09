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
        minHeap = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(minHeap, [distance, i, j])
        
        unionFind = UnionFind(len(points))
        res = 0
        mst = []

        while minHeap and len(mst) < len(points)-1:
            weight, n1, n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1, n2):
                continue
            res += weight
            mst.append([n1, n2])
        
        return res if len(mst) == len(points)-1 else -1

