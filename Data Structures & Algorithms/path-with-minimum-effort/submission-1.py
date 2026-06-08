class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # djikstars algo

        minHeap = [[0, 0, 0]] # diff, row, col
        visited = set()
        res = 0

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)
            if (row, col) in visited:
                continue
            res = max(res, diff)
            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return res
            for r, c in dirs:
                newRow = row + r
                newCol = col + c
                if 0 <= newRow < len(heights) and 0 <= newCol < len(heights[0]):
                    diff = abs(heights[row][col] - heights[newRow][newCol])
                    heapq.heappush(minHeap, [diff, newRow, newCol])
            visited.add((row, col))

        
            
