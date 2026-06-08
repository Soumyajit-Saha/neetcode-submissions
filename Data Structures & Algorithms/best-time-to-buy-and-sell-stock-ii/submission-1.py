class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        min_ = prices[0]

        for i in range(1, len(prices)):
            min_ = min(min_, prices[i] - dp[i - 1])
            dp[i] = max(prices[i] - min_, dp[i - 1])
        
        return dp[-1]