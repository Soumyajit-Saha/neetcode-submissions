class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = {}
        for i in range(len(matrix)):
            rowSum = 0
            for j in range(len(matrix[0])):
                rowSum += matrix[i][j]
                if i > 0:
                    self.prefixSum[(i, j)] = rowSum + self.prefixSum[(i - 1, j)]
                else:
                    self.prefixSum[(i, j)] = rowSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefixSum[(row2, col2)]
        above = self.prefixSum[(row1 - 1, col2)] if row1 > 0 else 0
        left = self.prefixSum[(row2, col1 - 1)] if col1 > 0 else 0
        topLeft = self.prefixSum[(row1 - 1, col1 - 1)] if row1 > 0 and col1 > 0 else 0
        return total - left - above + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)