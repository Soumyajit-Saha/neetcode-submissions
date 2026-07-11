class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)

        for i in range(len(queries)):
            queries[i] = (queries[i], i)

        queries.sort()

        intervals.sort()

        i = 0
        minHeap = []

        for j in range(len(queries)):
            while i < len(intervals) and intervals[i][0] <= queries[j][0]:
                l = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, [l, intervals[i][0], intervals[i][1]])
                i += 1

            while minHeap and minHeap[0][2] < queries[j][0]:
                heapq.heappop(minHeap)

            res[queries[j][1]] = minHeap[0][0] if minHeap else -1

        return res