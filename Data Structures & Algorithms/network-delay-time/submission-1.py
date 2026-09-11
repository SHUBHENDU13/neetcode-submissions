class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(n + 1):
            adj[i] = []
        
        for n1, n2, t in times:
            adj[n1].append([n2, t])

        time = {}
        minheap = [[0,k]]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in time:
                continue
            
            time[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in time:
                    heapq.heappush(minheap, [w1 + w2, n2])
        
        if len(time) != n:
            return -1

        maxtime = -1
        for n in time:
            maxtime = max(maxtime, time[n])
        return maxtime
            
        