class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # djikstars algo

        minHeap = [[0, 0, 0]] # diff, row, col
        visited = set()

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)
            if (row, col) in visited:
                continue
            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return diff
            for r, c in dirs:
                newRow = row + r
                newCol = col + c
                if 0 <= newRow < len(heights) and 0 <= newCol < len(heights[0]):
                    maxDiff = max(diff, abs(heights[row][col] - heights[newRow][newCol]))
                    heapq.heappush(minHeap, [maxDiff, newRow, newCol])
            visited.add((row, col))

        
            
