class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst, weight in edges:
            adj[src].append([dst, weight])
            adj[dst].append([src, weight])

        visit = set()
        minHeap = []
        res = 0

        visit.add(0)
        for neighbour, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbour])

        while minHeap:
            weight, src, node = heapq.heappop(minHeap)
            if node in visit:
                continue

            visit.add(node)
            res += weight

            for neighbour, weight in adj[node]:
                if neighbour not in visit:
                    heapq.heappush(minHeap, [weight, node, neighbour])
        
        return res if len(visit) == n else -1

