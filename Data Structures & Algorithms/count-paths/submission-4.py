class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        
        def dp(r, c):
            if (r >= m or c >= n):
                return 0
            if (r == m - 1 and c == n - 1):
                return 1

            if (r,c) in cache:
                return cache[(r,c)]

            right = dp(r, c + 1)
            bot = dp(r + 1, c)
            cache[(r,c)] = right + bot
            return cache[(r, c)]
        
        return dp(0,0)