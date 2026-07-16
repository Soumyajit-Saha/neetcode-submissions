class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for r, c in dirs:
                newRow, newCol = row + r, col + c
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] > grid[row][col]:
                    grid[newRow][newCol] = min(grid[newRow][newCol], 1 + grid[row][col])

                    queue.append((newRow, newCol))

            