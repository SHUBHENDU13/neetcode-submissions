class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = 1 + map.get(n, 0)
        
        heap = []
        for n in map:
            heapq.heappush(heap, [map[n], n])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res