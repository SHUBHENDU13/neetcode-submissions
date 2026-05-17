class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for row in range(len(matrix)):
            total = 0
            for col in range(len(matrix[0])):
                total += matrix[row][col]
                self.prefix[row][col] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2+1):
            rightMax = self.prefix[r][col2]
            leftMax = self.prefix[r][col1-1] if col1 > 0 else 0
            res += rightMax - leftMax
        return res

# param_1 = obj.sumRegion(row1,col1,row2,col2)