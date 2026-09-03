class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = {}

        def dp(i, capacity):
            if i == len(profit):
                return 0

            if (i, capacity) in cache:
                return cache[(i, capacity)]

            maxProfit = dp(i + 1, capacity)

            newCap = capacity - weight[i]
            if newCap >= 0:
                p1 = profit[i] + dp(i, newCap)
                p2 = profit[i] + dp(i + 1, newCap)
                maxProfit = max(maxProfit, p1, p2)
            cache[(i, capacity)] = maxProfit
            return cache[(i, capacity)]
        
        return dp(0, capacity)
