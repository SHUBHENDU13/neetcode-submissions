class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        path = set()
        minheap = [[grid[0][0],[0,0]]]
        while minheap:
            w, crd = heapq.heappop(minheap)
            r, c = crd
            if r == ROWS - 1 and c == COLS - 1:
                path.add(w)
                break
            # if (r, c) in visit:
            #     continue
            visit.add((r, c))
            path.add(w)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or
                    (nr, nc) in visit):
                    continue
                heapq.heappush(minheap, [grid[nr][nc], [nr, nc]])

        return max(path)
            