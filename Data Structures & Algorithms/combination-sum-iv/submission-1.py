class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {target: 1}

        def dfs(total):
            if total in dp:
                return dp[total]
            
            ways = 0
            for i in range(len(nums)):
                if total + nums[i] > target:
                    break
                ways += dfs(total + nums[i])
            dp[total] = ways

            return dp[total]

        return dfs(0)