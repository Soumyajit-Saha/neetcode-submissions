class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        # dp stores the no of combination possible to form given sum
        dp = {0: 1}

        def dfs(total):
            if total in dp:
                return dp[total]
            
            ways = 0
            for i in range(len(nums)):
                # We cannot remove nums[i] from target]
                if nums[i] > total:
                    break
                ways += dfs(total - nums[i])
            dp[total] = ways

            return dp[total]

        return dfs(target)