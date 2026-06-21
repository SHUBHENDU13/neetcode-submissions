class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        visit.add((0,0))
        queue.append((0,0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if (r == ROWS -1 and c == COLS - 1):
                    return length

                directions = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or r + dr >= ROWS or c + dc >= COLS or
                        (r + dr, c + dc) in visit or grid[r+dr][c+dc] == 1):
                        continue
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))
            length += 1
        return -1