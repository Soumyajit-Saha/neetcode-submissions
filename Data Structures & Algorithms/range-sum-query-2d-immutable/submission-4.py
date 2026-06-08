class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rangeMat = matrix

        curr = 0
        for j in range(len(matrix[0])):
            curr += matrix[0][j]
            self.rangeMat[0][j] = curr

        for i in range(1, len(matrix)):
            curr = 0
            for j in range(len(matrix[0])):
                curr += matrix[i][j]
                self.rangeMat[i][j] = curr + self.rangeMat[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.rangeMat[row2][col2]
        top = 0 if row1 - 1 < 0 else self.rangeMat[row1 - 1][col2]
        left = 0 if col1 - 1 < 0 else self.rangeMat[row2][col1 - 1]
        topLeft = 0 if (col1 - 1 < 0 or row1 - 1 < 0) else self.rangeMat[row1 - 1][col1 - 1]

        return total - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)