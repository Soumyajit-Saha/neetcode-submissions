class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dp = [1] * n

        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                dp[i + 1] = 1 + dp[i]
            
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                dp[i - 1] = max(dp[i - 1], 1 + dp[i])

        return sum(dp)