class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            if i < 0 or i == n or j < 0 or j == m or grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            return val + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    res = max(res, dfs(i, j))
        
        return res
