class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        res = 0

        minHeap = []

        minHeap.append((0, 0))

        while minHeap and len(visited) != len(points):
            dist, nearestPoint = heapq.heappop(minHeap)
            if nearestPoint in visited:
                continue
            
            visited.add(nearestPoint)
            res += dist
            for i in range(len(points)):
                if i not in visited:
                    d = abs(points[nearestPoint][0] - points[i][0]) + abs(points[nearestPoint][1] - points[i][1])
                    heapq.heappush(minHeap, (d, i))

        return res

