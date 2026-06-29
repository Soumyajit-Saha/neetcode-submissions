class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        half = total // 2

        dp = [[0] * (half + 1) for _ in range(len(stones) + 1)]

        for i in range(1, len(stones) + 1):
            for j in range(1, half + 1):
                if stones[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], stones[i - 1] + dp[i - 1][j - stones[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]

        return total - dp[-1][-1] - dp[-1][-1]