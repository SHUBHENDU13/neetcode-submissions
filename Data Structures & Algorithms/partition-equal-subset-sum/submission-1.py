class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        
        def dp(i, sum1, sum2):
            if i == len(nums):
                return True if sum1 == sum2 else False

            state = (i, sum1)
            if state in cache:
                return cache[state]

            left = dp(i + 1, sum1 + nums[i], sum2)
            right = dp(i + 1, sum1, sum2 + nums[i])
            cache[state] = left or right
            return cache[state]

        return dp(0,0,0)