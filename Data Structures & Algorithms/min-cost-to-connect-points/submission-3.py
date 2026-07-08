class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # consider every point as node like 
        # Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
        # (0,0) -> 0, (2,2) -> 1, .... where 0,1,2... are nodes
        # then simply run mst to find min distance between nodes
        adj = {}
        for i in range(len(points)):
            adj[i] = []

        for i in range(len(points)):
            for j in range(len(points)):
                if j == i:
                    continue
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, distance])

        visit = set()
        minHeap = []

        visit.add(0)
        for neighbour, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbour])

        res = 0

        while minHeap:
            weight, src, node = heapq.heappop(minHeap)
            if node in visit:
                continue

            visit.add(node)
            res += weight

            for neighbour, weight in adj[node]:
                if neighbour not in visit:
                    heapq.heappush(minHeap, [weight, node, neighbour])

        return res