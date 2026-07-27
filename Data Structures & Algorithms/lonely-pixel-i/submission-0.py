class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows, cols = len(picture), len(picture[0])
        row_count = [0] * rows
        col_count = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    res += 1
        
        return res