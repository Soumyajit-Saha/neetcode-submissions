class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev_dp = [0] * n
        for col in range(n):
            if obstacleGrid[0][col] == 1:
                break
            prev_dp[col] = 1

        for i in range(1, m):
            new_dp = [0] * n
            if obstacleGrid[i][0] != 1 and prev_dp[0] != 0:
                new_dp[0] = 1
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                new_dp[j] = new_dp[j - 1] + prev_dp[j]

            prev_dp = new_dp

        return prev_dp[-1]