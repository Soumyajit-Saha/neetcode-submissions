class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            adjList[u].append((t, v))
        
        minHeap = [(0, k)]
        res = float('-inf')

        visited = set()

        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            
            res = max(res, dist)
            for d, nei in adjList[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (dist + d, nei))
        
        return res if len(visited) == n else -1

