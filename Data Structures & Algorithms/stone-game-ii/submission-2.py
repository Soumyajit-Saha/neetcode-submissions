class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(alice, i, M):
            # Gives us the max score Alice can get
            if i == len(piles):
                return 0
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]
            

            res = 0 if alice else float('inf') # we need to maximize in Alice turn and minimize in Bob's turn
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                if alice:
                    total += piles[i + X - 1]
                    res = max(res, total + dfs(not alice, X + i, max(M, X)))
                else:
                    total -= piles[i + X - 1]
                    res = min(res, dfs(not alice, X + i, max(M, X)))

            dp[(alice, i, M)] = res
            return res

        return dfs(True, 0, 1)