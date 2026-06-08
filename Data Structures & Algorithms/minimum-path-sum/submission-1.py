class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        prev_dp = [0] * len(grid[0])
        total = 0
        for j in range(len(grid[0])):
            total += grid[0][j]
            prev_dp[j] = total

        for i in range(1, len(grid)):
            new_dp = [0] * len(grid[0])
            new_dp[0] = prev_dp[0] + grid[i][0]
            for j in range(1, len(grid[0])):
                new_dp[j] = min(new_dp[j - 1], prev_dp[j]) + grid[i][j]
            prev_dp = new_dp

        return prev_dp[-1]