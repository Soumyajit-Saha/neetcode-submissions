class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_dp = [1] * n

        for i in range(1, m):
            new_dp = [1] * n
            for j in range(1, n):
                new_dp[j] = new_dp[j - 1] + prev_dp[j]
            prev_dp = new_dp

        return prev_dp[-1] 
