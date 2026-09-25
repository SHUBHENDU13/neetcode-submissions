class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()

        found = False
        for r in range(ROWS):
            if found:
                break
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.findIsland(r, c, ROWS, COLS, visit, grid, directions)
                    found = True
                    break

        q = deque([r, c, 0] for r, c in visit)

        while q:
            for _ in range(len(q)):
                r, c, path = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit):
                        continue
                    if grid[nr][nc] == 1:
                        return path
                    visit.add((nr, nc))
                    q.append([nr, nc, path + 1])

        return -1

    def findIsland(self, r, c, ROWS, COLS, visit, grid, directions):
        if (min(r, c) < 0 or r >= ROWS or c >= COLS or
            (r, c) in visit or grid[r][c] == 0):
            return 
        visit.add((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            self.findIsland(nr, nc, ROWS, COLS, visit, grid, directions)