class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        # all possible sums in range [-total, + total]
        if target < -totalSum or target > totalSum:
            return 0
        dp = [[0] * (2 * totalSum + 1) for i in range(len(nums) + 1)]

        dp[0][0 + totalSum] = 1

        for i in range(1, len(nums) + 1):
            for j in range(2 * totalSum + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
                if j + nums[i - 1] < (2 * totalSum + 1):
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]


        return dp[-1][totalSum + target]
