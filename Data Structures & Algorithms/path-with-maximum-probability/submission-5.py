class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        probabilities = {}
        minheap = [[-1, start_node]]
        while minheap:
            prob, node = heapq.heappop(minheap)
            if node in probabilities:
                continue
            probabilities[node] = -prob
            if node == end_node:
                break
            for node2, prob2 in adj[node]:
                if node2 not in probabilities:
                    heapq.heappush(minheap, [-(-prob * prob2), node2])
        
        return probabilities[end_node] if end_node in probabilities else 0