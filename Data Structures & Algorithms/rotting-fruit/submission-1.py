class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        res = 0
        while fresh and queue:
            size = len(queue)
            while size:
                row, col = queue.popleft()
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for r, c in dirs:
                    newRow, newCol = row + r, col + c
                    if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh -= 1
                size -= 1
            res += 1

        return res if fresh == 0 else -1
