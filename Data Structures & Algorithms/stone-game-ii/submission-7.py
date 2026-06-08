class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(Alice, i, M):
            if i == len(piles):
                return 0
            if (Alice, i, M) in dp:
                return dp[(Alice, i, M)]
            res = float('-inf') if Alice else float('inf')

            curr = 0
            for X in range(1, 2*M + 1):
                if i + X > len(piles):
                    break
                curr += piles[i + X - 1]
                if Alice:
                    res = max(res, curr + dfs(not Alice, i + X, max(X, M)))
                else:
                    res = min(res, dfs(not Alice, i + X, max(X, M)))
            dp[(Alice, i, M)] = res
            return dp[(Alice, i, M)]

        return dfs(True, 0, 1)
