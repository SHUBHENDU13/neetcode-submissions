class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(n + 1):
            adj[i] = []
        for s, d, w in times:
            adj[s].append([d, w])

        times = {}
        minheap = [[0,k]]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in times:
                continue
            times[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in times:
                    heapq.heappush(minheap, [w1 + w2, n2])

        if len(times) != n:
            return -1
        
        maxtime = 0
        for n in times:
            maxtime = max(maxtime, times[n])
        return maxtime