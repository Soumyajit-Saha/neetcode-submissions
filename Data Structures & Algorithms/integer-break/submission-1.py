class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}

        def dfs(num):
            if num == 1:
                return 1
            if num in dp:
                return dp[num]

            res = num if num != n else 0
            for i in range(1, num):
                res = max(res, i * dfs(num - i))
            
            dp[num] = res
            return dp[num]

        return dfs(n)