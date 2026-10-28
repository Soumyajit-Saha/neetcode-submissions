class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row_count = {i: 0 for i in range(len(grid))}
        col_count = {i: 0 for i in range(len(grid[0]))}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        res += 1

        return res