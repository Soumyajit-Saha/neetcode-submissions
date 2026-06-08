class Solution:
    def totalNQueens(self, n: int) -> int:
        res = [0] * n
        count = [0]

        def check(row, col):
            for r in range(row):
                if col == res[r] or abs(col - res[r]) == abs(row - r):
                    return False
            return True

        def NQ(row):
            for j in range(n):
                if check(row, j):
                    res[row] = j
                    if row == n - 1:
                        count[0] += 1
                    else:
                        NQ(row + 1)

        NQ(0)
        return count[0]