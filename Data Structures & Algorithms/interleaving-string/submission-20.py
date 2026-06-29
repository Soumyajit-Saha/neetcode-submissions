class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        dp[0][0] = True

        for i in range(1, len(s2) + 1):
            if s3[i + 0 - 1] == s2[i - 1]:
                dp[i][0] = dp[i - 1][0]

        for j in range(1, len(s1) + 1):
            if s3[0 + j - 1] == s1[j - 1]:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                if s3[i + j - 1] == s1[j - 1]:
                    dp[i][j] = dp[i][j - 1]
                if dp[i][j]:
                    continue
                if s3[i + j - 1] == s2[i - 1]:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]