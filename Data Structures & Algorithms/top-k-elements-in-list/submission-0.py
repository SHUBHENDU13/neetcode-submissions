class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1
        
        max_heap = []
        for n in map:
            heapq.heappush(max_heap, [-map[n], n])

        res = []
        for i in range(k):
            count, n = heapq.heappop(max_heap)
            res.append(n)

        return res