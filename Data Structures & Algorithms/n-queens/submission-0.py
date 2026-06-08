class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        ans = []
        ansMap = {}

        for i in range(n):
            rep = ['.' for _ in range(n)]
            rep[i] = 'Q'
            ansMap[i] = ''.join(rep)

        def check(row, col):
            for r in range(row):
                if ans[r] == col or abs(row - r) == abs(ans[r] - col):
                    return False
            return True

        def NQ(row):
            for col in range(n):
                if check(row, col):
                    ans.append(col)
                    if row == n - 1:
                        res.append([ansMap[i] for i in ans.copy()])
                    else:
                        NQ(row + 1)
                    ans.pop()

        NQ(0)
        return res

