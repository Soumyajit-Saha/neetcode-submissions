class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort()

        i = 0
        minHeap = []

        res = [-1] * len(queries)

        for j in range(len(queries)):
            while i < len(intervals) and intervals[i][0] <= queries[j][0]:
                l = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, [l, intervals[i][0], intervals[i][1]])
                i += 1

            while minHeap and minHeap[0][2] < queries[j][0]:
                heapq.heappop(minHeap)

            if minHeap:
                res[queries[j][1]] = minHeap[0][0]

        return res

            