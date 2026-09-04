class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = {}

        def dfs(i, capacity):
            if i == len(profit):
                return 0

            if (i, capacity) in cache:
                return cache[(i, capacity)]

            maxprofit = dfs(i+1, capacity)
            newCap = capacity - weight[i]
            if newCap >= 0:
                maxprofit = max(maxprofit, profit[i] + dfs(i, newCap))
            cache[(i, capacity)] = maxprofit
            return cache[(i, capacity)]

        return dfs(0, capacity)
