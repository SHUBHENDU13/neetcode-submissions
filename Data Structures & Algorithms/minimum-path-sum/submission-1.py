class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        cache = {}
        
        def dp(r, c):
            if r == M - 1 and c == N - 1:
                return grid[r][c]
            if r >= M or c >= N:
                return float('inf')

            if (r, c) in cache:
                return cache[(r, c)]

            right = dp(r, c + 1)
            bot = dp(r + 1, c)
            cache[(r, c)] = grid[r][c] + min(right, bot)
            return cache[(r, c)]

        return dp(0,0)

            