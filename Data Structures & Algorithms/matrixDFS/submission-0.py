class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == 1):
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r, c))
            path = 0
            for dr, dc in directions:
                path += dfs(r + dr, c + dc)
            visit.remove((r, c))
            return path

        return dfs(0,0)