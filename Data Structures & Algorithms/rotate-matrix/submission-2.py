class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1

        while l < r:
            for k in range(r - l):

                t = l
                b = r

                tmp = matrix[t][l + k]
                matrix[t][l + k] = matrix[b - k][l]
                matrix[b - k][l] = matrix[b][r - k]
                matrix[b][r - k] = matrix[t + k][r]
                matrix[t + k][r] = tmp
            l += 1
            r -= 1

        