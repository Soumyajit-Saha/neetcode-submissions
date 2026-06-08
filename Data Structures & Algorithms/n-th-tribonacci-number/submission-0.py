class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}

        def trib(n):
            if n in dp:
                return dp[n]
            if n == 0:
                return 0
            if n <= 2:
                return 1
            
            dp[n] = trib(n - 1) + trib(n - 2) + trib(n - 3)
            return dp[n]

        return trib(n)