class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        ans = 0
        for i in range(k):
            ans = heapq.heappop(nums)
        return ans*(-1)
