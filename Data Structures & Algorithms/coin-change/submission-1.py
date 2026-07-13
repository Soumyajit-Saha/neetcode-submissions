class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        coins.sort()

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            res = float('inf')
            for coin in coins:
                if coin > amount:
                    break
                res = min(res, 1 + dfs(amount - coin))
            dp[amount] = res
            return dp[amount]

        res = dfs(amount)
        return res if res != float('inf') else -1
