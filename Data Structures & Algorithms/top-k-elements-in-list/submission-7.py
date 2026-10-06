class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        minheap = []
        for n in count:
            heapq.heappush(minheap, [count[n], n])
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res