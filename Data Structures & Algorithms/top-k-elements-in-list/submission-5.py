class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        maxheap = []
        for key, value in count.items():
            heapq.heappush(maxheap, [-value, key])
        res = []
        while k > 0:
            value, key = heapq.heappop(maxheap)
            res.append(key)
            k -= 1
        return res