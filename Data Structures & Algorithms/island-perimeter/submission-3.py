class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs call gives the perimeter starting from that node
        # if we call dfs from a node, we don't count the shared side as that gets skiped dues to visited
        # baically we count the boundary cells
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
                # It is a perimeter as it forms a boundary
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            res = dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)
            # visited.remove((i, j))
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)

        return 0