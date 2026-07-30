class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        minheap = []
        for key, value in hashmap.items():
            heapq.heappush(minheap, [-value, key])
        res = []
        while k > 0:
            poped_item = heapq.heappop(minheap)
            res.append(poped_item[1])
            k -= 1
        return res