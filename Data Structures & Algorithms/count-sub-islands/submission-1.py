class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        sys.setrecursionlimit(300000)
        ROWS, COLS = len(grid1), len(grid1[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or grid2[r][c] == 0):
                return True
            
            visit.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                res = dfs(nr, nc) and res
            
            return res

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r, c) not in visit and dfs(r, c):
                    count += 1
        
        return count

            