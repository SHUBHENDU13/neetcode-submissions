class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gMax, gMin = nums[0], nums[0]
        cMax, cMin = 0, 0
        total = 0

        for n in nums:
            cMax = max(cMax + n, n)
            cMin = min(cMin + n, n)
            total += n

            gMax = max(gMax, cMax)
            gMin = min(gMin, cMin)

        return max(gMax, total - gMin) if gMax > 0 else gMax