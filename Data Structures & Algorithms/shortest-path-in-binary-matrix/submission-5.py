class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))
        length = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == N - 1 and c == N - 1:
                    return length
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr >= N or nc >= N or
                        (nr, nc) in visit or grid[nr][nc] == 1):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1


