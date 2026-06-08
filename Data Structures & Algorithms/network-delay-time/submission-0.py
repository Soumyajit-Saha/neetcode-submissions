class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = {i: [] for i in range(1, n + 1)}

        for time in times:
            u = time[0]
            v = time[1]
            dist = time[2]
            adjList[u].append((dist, v))
        
        visited = set()

        minHeap = []

        minHeap.append((0, k))

        res = 0

        while minHeap:
            dist, nearestNode = heapq.heappop(minHeap)
            if nearestNode in visited:
                continue
            res = max(res, dist)
            for d, nei in adjList[nearestNode]:
                heapq.heappush(minHeap, (dist + d, nei))

            visited.add(nearestNode)

        return res if len(visited) == n else -1
            
