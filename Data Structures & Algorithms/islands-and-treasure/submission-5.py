class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0],[-1,0],[0,1],[0,-1]]
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c, 0])

        while q:
            for _ in range(len(q)):
                r, c, path = q.popleft()
                if (r, c) in visit:
                    continue
                visit.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit or grid[nr][nc] == -1):
                        continue
                    grid[nr][nc] = min(grid[nr][nc], 1 + path)
                    q.append([nr, nc, 1 + path])