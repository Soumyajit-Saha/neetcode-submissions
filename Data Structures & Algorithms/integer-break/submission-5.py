class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def dfs(num):
            if num == 1:
                return 1
            if num in dp:
                return dp[num]
            res = 0 if num == n else num
            for i in range(1, num):
                res = max(res, i * dfs(num - i))
            dp[num] = res
            return dp[num]
        
        return dfs(n)