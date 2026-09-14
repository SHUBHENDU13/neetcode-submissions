class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst, w in edges:
            adj[src].append([dst, w])
            adj[dst].append([src, w])

        mst = []
        res = 0

        visit = set()
        minheap = []
        visit.add(0)
        for nei, w in adj[0]:
            heapq.heappush(minheap, [w, 0, nei])

        while minheap:
            w1, s1, d1 = heapq.heappop(minheap)
            if d1 in visit:
                continue
            mst.append([s1, d1])
            visit.add(d1)
            res += w1
            for d2, w2 in adj[d1]:
                if d2 not in visit:
                    heapq.heappush(minheap, [w2, d1, d2])

        return res if len(visit) == n else -1
        
        