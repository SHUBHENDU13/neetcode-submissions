class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, distance])
                adj[j].append([i, distance])

        visit = set()
        mst = []
        res = 0
        minheap = []
        visit.add(0)
        for dst, w in adj[0]:
            heapq.heappush(minheap, [w, 0, dst])

        while minheap:
            w1, s1, d1 = heapq.heappop(minheap)
            if d1 in visit:
                continue
            visit.add(d1)
            mst.append([s1, d1])
            res += w1
            for d2, w2 in adj[d1]:
                if d2 not in visit:
                    heapq.heappush(minheap, [w2, d1, d2])

        return res
