class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        queries = [(q, i) for i, q in enumerate(queries)]

        queries.sort()

        res = [-1] * len(queries)
        minHeap = []

        for q, i in queries:
            for interval in intervals:
                if interval[0] <= q:
                    length = interval[1] - interval[0] + 1
                    heapq.heappush(minHeap, (length, interval[1]))

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[i] = minHeap[0][0] if minHeap else -1

        return res
            