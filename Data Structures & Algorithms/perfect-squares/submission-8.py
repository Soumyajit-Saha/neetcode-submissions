class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}

        def dfs(num):
            if num == 1 or num == 0:
                return num
            if num in dp:
                return dp[num]
            
            i = 1
            res = num
            while i * i <= num:
                res = min(res, 1 + dfs(num - i * i))
                i += 1

            dp[num] = res
            return dp[num]
        
        return dfs(n)