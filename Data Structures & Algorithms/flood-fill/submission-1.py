class Solution:

    def dfs(self, image, r, c, originalColor, visit, cellsToColor):
        ROWS, COLS = len(image), len(image[0])
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
            image[r][c] != originalColor or (r,c) in visit):
            return

        cellsToColor.append([r,c])
        visit.add((r,c))
        self.dfs(image, r+1, c, originalColor, visit, cellsToColor)
        self.dfs(image, r-1, c, originalColor, visit, cellsToColor)
        self.dfs(image, r, c+1, originalColor, visit, cellsToColor)
        self.dfs(image, r, c-1, originalColor, visit, cellsToColor)

        return cellsToColor

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cellsToColor = []
        originalColor = image[sr][sc]
        self.dfs(image, sr, sc, originalColor, set(), cellsToColor)
        for i in cellsToColor:
            r,c = i
            image[r][c] = color

        return image