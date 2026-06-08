class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        def dfs(i):
            if dp[i]:
                return dp[i]
            if s[i] == '0':
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and  s[i + 1] in set(['0', '1', '2', '3', '4', '5', '6']))):
                res += dfs(i + 2)
            dp[i] = res
            return dp[i]

        return dfs(0)
