class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        n = len(matrix)
        m = len(matrix[0])

        curr = 0
        for j in range(m):
            curr += self.mat[0][j]
            self.mat[0][j] = curr

        for i in range(1, n):
            curr = 0
            for j in range(m):
                curr += self.mat[i][j]
                self.mat[i][j] = self.mat[i - 1][j] + curr
        
 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.mat[row2][col2]
        top = self.mat[row1 - 1][col2] if row1 > 0 else 0
        left = self.mat[row2][col1 - 1] if col1 > 0 else 0
        topLeft = self.mat[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return total - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)