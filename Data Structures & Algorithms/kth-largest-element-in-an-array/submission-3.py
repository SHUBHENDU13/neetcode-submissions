class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        # nums = [-n for n in nums]
        # heapq.heapify(nums)

        # ans = 0
        # for i in range(k):
        #     ans = heapq.heappop(nums)
        
        # return -ans