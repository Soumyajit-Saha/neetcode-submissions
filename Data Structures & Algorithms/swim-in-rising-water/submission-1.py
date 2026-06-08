class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Idea is similar to Djikstra's algo
        # We put the time (along with the coordinates of the grid), at which that cell in the grid can be reached, in the minHeap
        # Suppose the current cell can be reached at t time, we can reach its neighboring cells in max(t, time when the water rises to that height, i.e the height of that cell)
        # We put that time along with the coordinates of the neighbors in the minHeap
        # We keep on getting the lowest time/height cell from minHeap
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
