class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        adj = {}
        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            s,d = edges[i]
            prob = succProb[i]
            adj[s].append([d, prob])
            adj[d].append([s, prob])

        visit = set()

        # starting -> -ve 1 as prob is maintained -ve and maxProb can be 1, 
        # so when we multiply any less prob, it'll only decrease
        maxHeap = [[-1, start_node]]
        while maxHeap:
            p1, n1 = heapq.heappop(maxHeap)
            if n1 == end_node:
                return -p1
            visit.add(n1)
            
            for n2, p2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(maxHeap, [-(-p1 * p2), n2])
        return 0