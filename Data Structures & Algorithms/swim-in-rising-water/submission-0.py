class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        visit = set()
        minHeap = [[grid[0][0],0,0]]
        visit.add((0,0))
        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return h
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or 
                    neiR >= N or neiC >= N
                    or (neiR, neiC) in visit):
                    continue
                heapq.heappush(minHeap, [max(h, grid[neiR][neiC]), neiR, neiC])
                visit.add((neiR, neiC))
        return -1


        