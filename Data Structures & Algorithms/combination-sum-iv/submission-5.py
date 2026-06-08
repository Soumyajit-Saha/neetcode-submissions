class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Coin change 2, but we need to consider (1, 3) and (3, 1) as separate unlike coin change 2
        # So, we run target loop first
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for t in range(1, target + 1):
            for coin in nums:
                if coin > t:
                    break
                dp[t] += dp[t - coin]
        
        return dp[-1]