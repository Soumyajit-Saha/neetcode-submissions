class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        firstRow = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRow = 0
                    else:
                        matrix[i][0] = 0

                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
        if firstRow == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0



        
        