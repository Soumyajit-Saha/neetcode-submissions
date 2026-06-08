class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n - 1

        top = 0
        bottom = n - 1

        mat = [[0] * n for _ in range(n)]

        val = 1

        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                mat[top][j] = val
                val += 1
            
            top += 1


            for i in range(top, bottom + 1):
                mat[i][right] = val
                val += 1
            
            right -= 1


            if top <= bottom:
                for j in range(right, left - 1, -1):
                    mat[bottom][j] = val
                    val += 1
            
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    mat[i][left] = val
                    val += 1
            
                left += 1

        return mat