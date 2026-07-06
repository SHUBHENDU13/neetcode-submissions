class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []

        for src, dst, weight in edges:
            adj[src].append([dst, weight])
            adj[dst].append([src, weight])

        mst = []
        res = 0

        visit = set()
        minHeap = []

        visit.add(0)
        for neighbour, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbour])

        while minHeap:
            weight, src, node = heapq.heappop(minHeap)
            if node in visit:
                continue

            mst.append([src, node])
            res += weight
            visit.add(node)

            for neighbour, weight in adj[node]:
                if neighbour not in visit:
                    heapq.heappush(minHeap, [weight, node, neighbour])

        return res if len(visit) == n else -1
