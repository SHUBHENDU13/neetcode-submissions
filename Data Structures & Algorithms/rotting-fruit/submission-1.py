class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    if (min(r+dr, c+dc) < 0 or r+dr >= ROWS or c+dc >= COLS or
                        grid[r+dr][c+dc] != 1):
                        continue
                    grid[r+dr][c+dc] = 2
                    queue.append((r+dr, c+dc))
                    fresh -= 1
            time += 1

        return time if not fresh else -1

        