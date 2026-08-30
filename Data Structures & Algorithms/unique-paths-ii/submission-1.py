class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}
        
        def dp(r, c):
            if (r >= ROWS or c >= COLS or min(r, c) < 0 or obstacleGrid[r][c] == 1):
                return 0

            if (r == ROWS - 1 and c == COLS - 1):
                return 1

            if (r, c) in cache:
                return cache[(r, c)]

            right = dp(r, c + 1)
            bot = dp(r + 1, c)
            cache[(r, c)] = right + bot
            return cache[(r, c)]

        return dp(0,0)
