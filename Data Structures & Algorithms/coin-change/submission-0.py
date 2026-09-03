class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dp(i, amount):
            if amount == 0:
                return 0
            if i == len(coins):
                return float('inf')

            if (i, amount) in cache:
                return cache[(i, amount)]

            total = dp(i + 1, amount)
            newAmt = amount - coins[i]
            if newAmt >= 0:
                tmp = 1 + dp(i, newAmt)
                total = min(total, tmp)
            cache[(i, amount)] = total
            return cache[(i, amount)]
        
        res = dp(0, amount)
        return res if res != float('inf') else -1