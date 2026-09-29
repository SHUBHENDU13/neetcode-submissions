class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visit = set()

        total_land = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if min(r, c) == 0 or r == ROWS - 1 or c == COLS - 1:
                        q.append([r, c])
                    total_land += 1
        
        visit = set()
        while q:
            r, c = q.popleft()
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or
                    (nr, nc) in visit or grid[nr][nc] == 0):
                    continue
                q.append([nr, nc])

        return total_land - len(visit)
