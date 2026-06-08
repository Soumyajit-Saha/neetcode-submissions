class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        visited = set()

        minHeap.append([grid[0][0], 0, 0])

        while minHeap:
            time, row, col = heapq.heappop(minHeap)
            if (row, col) in visited:
                continue
            if row == len(grid) - 1 and col == len(grid) - 1:
                return time
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for r, c in dirs:
                newRow = row + r
                newCol = col + c

                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid):
                    heapq.heappush(minHeap, [max(time, grid[newRow][newCol]), newRow, newCol])

            visited.add((row, col))
