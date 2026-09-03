import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2)

        cache = {}

        def dp(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))

            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = min(
                                    dp(i + 1, total), 
                                    dp(i + 1, total + stones[i])
                                )
            return cache[(i, total)]

        return dp(0,0)