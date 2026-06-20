class Solution:

    def dfs(self, image, r, c, sr, sc, visit, cellsToColor):
        ROWS, COLS = len(image), len(image[0])
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
            image[r][c] != image[sr][sc] or (r,c) in visit):
            return

        cellsToColor.append([r,c])
        visit.add((r,c))
        self.dfs(image, r+1, c, sr, sc, visit, cellsToColor)
        self.dfs(image, r-1, c, sr, sc, visit, cellsToColor)
        self.dfs(image, r, c+1, sr, sc, visit, cellsToColor)
        self.dfs(image, r, c-1, sr, sc, visit, cellsToColor)

        return cellsToColor

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cellsToColor = []
        self.dfs(image, sr, sc, sr, sc, set(), cellsToColor)
        for i in cellsToColor:
            r,c = i
            image[r][c] = color

        return image