class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        latestPowerOfTwo = 1
        
        for i in range(1, n + 1):
            if i == 2 * latestPowerOfTwo:
                latestPowerOfTwo = i

            dp[i] = 1 + dp[i - latestPowerOfTwo]

        return dp