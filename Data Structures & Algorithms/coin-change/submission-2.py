class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dfs(i, amount):
            if amount == 0:
                return 0
            if i == len(coins):
                return float('inf')

            if (i, amount) in cache:
                return cache[(i, amount)]

            res = dfs(i + 1, amount)
            newAmt = amount - coins[i]
            if newAmt >= 0:
                tmp = 1 + dfs(i, newAmt)
                res = min(res, tmp)
            cache[(i, amount)] = res
            return cache[(i, amount)]
        
        res = dfs(0, amount)
        return res if res != float('inf') else -1