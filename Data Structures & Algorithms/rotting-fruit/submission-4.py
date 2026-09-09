class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        q = deque()
        time = 0

        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                visit.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    visit.add((nr, nc))
                    q.append((nr, nc))
            time += 1

        return time if fresh == 0 else -1
