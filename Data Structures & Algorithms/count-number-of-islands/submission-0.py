class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()

        def dfs(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or (i, j) in visited or grid[i][j] == '0':
                return
            grid[i][j] = 0
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res
            