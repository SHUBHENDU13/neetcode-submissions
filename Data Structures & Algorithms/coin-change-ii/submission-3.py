class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if (i, amount) in cache:
                return cache[(i, amount)]

            res1 = dfs(i + 1, amount)
            newamt = amount - coins[i]
            res2 = 0
            if newamt >= 0:
                res2 = dfs(i, newamt)
            cache[(i, amount)] = res1 + res2
            return cache[(i, amount)]

        res = dfs(0, amount)
        return res