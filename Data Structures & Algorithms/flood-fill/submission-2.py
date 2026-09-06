class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        og_color = image[sr][sc]
        visit = set()

        def dfs(r, c, color):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or image[r][c] != og_color):
                return

            image[r][c] = color
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, color)

        dfs(sr, sc, color)

        return image