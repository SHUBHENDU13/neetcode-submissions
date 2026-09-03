class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)
        if numsSum % 2 != 0:
            return False
        target = numsSum // 2

        cache = {}

        def dp(i, total):
            if i == len(nums):
                return False
            if total == target:
                return True

            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = (
                                dp(i + 1, total) or 
                                dp(i + 1, total + nums[i])
                            )

            return cache[(i, total)]

        return dp(0,0)