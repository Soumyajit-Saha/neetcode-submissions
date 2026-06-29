class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(i, M, alice):
            if i == len(piles):
                return 0
            if (i, M, alice) in dp:
                return dp[(i, M, alice)]
            res = -float('inf') if alice else float('inf')

            curr = 0
            for X in range(1, 2*M + 1):
                ind = i + X - 1
                if ind == len(piles):
                    break
                curr += piles[ind]
                if alice:
                    res = max(res, curr + dfs(ind + 1, max(X, M), not alice))
                else:
                    res = min(res, dfs(ind + 1, max(X, M), not alice))
            
            dp[(i, M, alice)] = res
            return dp[(i, M, alice)]

        return dfs(0, 1, True)
