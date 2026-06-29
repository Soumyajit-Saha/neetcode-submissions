class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i] = max(dp[i - 1], prices[i] - prices[j] + dp[j - 2])

        dp = [0] * len(prices)
        min_ = prices[0]
        for i in range(1, len(prices)):
            min_ = min(min_, prices[i] - (dp[i - 2] if i >= 2 else 0))
            dp[i] = max(dp[i - 1], prices[i] - min_)

        return dp[-1]
