class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dp(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (i, total) in cache:
                return cache[(i, total)]

            add = dp(i + 1, total + nums[i])
            sub = dp(i + 1, total - nums[i])
            cache[(i, total)] = add + sub
            return cache[(i, total)]

        return dp(0, 0)