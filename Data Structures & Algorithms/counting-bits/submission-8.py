class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0] * (n + 1)
        dp[1] = 1
        latestPowerOfTwo = 2
        
        for i in range(2, n + 1):
            if i == 2 * latestPowerOfTwo:
                latestPowerOfTwo = i

            dp[i] = 1 + dp[i - latestPowerOfTwo]

        return dp