class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        visit.add((0,0))
        queue.append((0,0))

        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1):
                    return -1
                if (r == ROWS - 1 and c == COLS - 1):
                    return length

                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    if (r + dr < 0 or c + dc < 0 or r + dr >= ROWS or c + dc >= COLS or
                        (r +dr, c + dc) in visit or grid[r+dr][c+dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1

        return -1
                