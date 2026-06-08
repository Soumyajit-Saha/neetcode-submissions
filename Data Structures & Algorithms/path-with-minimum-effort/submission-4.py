class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minHeap = []
        minHeap.append([0, 0, 0])
        visited = set()
        n = len(heights)
        m = len(heights[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]


        while minHeap:
            effort, row, col = heapq.heappop(minHeap)
            if row == (n - 1) and col == (m - 1):
                return effort
            if (row, col) in visited:
                continue
            for r, c in dirs:
                newRow = row + r
                newCol = col + c
                if 0 <= newRow < n and 0 <= newCol < m:
                    diff = abs(heights[row][col] - heights[newRow][newCol])
                    heapq.heappush(minHeap, [max(diff, effort), newRow, newCol])
            visited.add((row, col))

        
