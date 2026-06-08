class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for idx, point in enumerate(points):
            dist = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
            minHeap.append((dist, idx))

        heapq.heapify(minHeap)

        res = []
        for i in range(k):
            _, idx = heapq.heappop(minHeap)
            res.append(points[idx])

        return res