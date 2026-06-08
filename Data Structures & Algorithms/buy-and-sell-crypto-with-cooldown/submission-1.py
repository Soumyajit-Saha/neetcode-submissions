class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        min_ = prices[0]

        for i in range(1, len(prices)):
            min_ = min(min_, prices[i] - dp[i - 2]) if i > 1 else min(min_, prices[i])
            dp[i] = max(dp[i], prices[i] - min_)
        
        return max(dp)