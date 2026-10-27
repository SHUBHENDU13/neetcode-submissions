class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        original_color = image[sr][sc]
        
        def dfs(r, c, color):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                image[r][c] != original_color or (r, c) in visit):
                return

            image[r][c] = color
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, color)

        dfs(sr, sc, color)
        return image
