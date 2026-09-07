class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        res = 0

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                (r,c) in visit or grid[r][c] == '0'):
                return 

            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    res += 1

        return res


            