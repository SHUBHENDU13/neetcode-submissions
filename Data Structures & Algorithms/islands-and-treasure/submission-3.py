class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visit = set()
        INF = 2147483647

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c, 0])

        while q:
            for _ in range(len(q)):
                r, c, path = q.popleft()
                if (r,c) in visit:
                    continue
                visit.add((r, c))
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or r + dr >= ROWS or 
                    c + dc >= COLS or (r + dr, c + dc) in visit 
                    or grid[r + dr][c + dc] == -1):
                        continue
                    grid[r + dr][c + dc] = min(grid[r + dr][c + dc], 1 + path)
                    q.append([r + dr, c + dc, 1 + path])
                
        
        