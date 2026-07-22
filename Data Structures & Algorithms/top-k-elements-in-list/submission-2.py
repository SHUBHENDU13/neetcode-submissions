class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []
        for n in count:
            heapq.heappush(heap, [count[n], n])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(len(heap)):
            freq, n = heapq.heappop(heap)
            res.append(n)

        return res
