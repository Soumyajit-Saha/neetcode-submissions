class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l, r, alice):
            if l > r:
                return 0
            if (l, r, alice) in dp:
                return dp[(l, r, alice)]
            res = float('-inf') if alice else float('inf')

            if alice:
                res = max(res, piles[l] + dfs(l + 1, r, not alice), piles[r] + dfs(l, r - 1, not alice))
            else:
                res = min(res, dfs(l + 1, r, not alice), dfs(l, r - 1, not alice))
            
            dp[(l, r, alice)] = res
            return dp[(l, r, alice)]

        res = dfs(0, len(piles) - 1, True)
        
        if res > (sum(piles) - res):
            return True
        else:
            return False