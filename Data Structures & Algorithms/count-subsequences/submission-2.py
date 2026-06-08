class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        # if we change the row and col to t and s resp, dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
        # As we need number of ways subsequence in s can form t, 
        # dp[i][j - 1] will be have no of ways we can get t[: j] without s[i]
        for i in range(len(s) + 1):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]