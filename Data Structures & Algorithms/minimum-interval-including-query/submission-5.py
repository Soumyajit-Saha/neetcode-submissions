class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Idea is to sort the queries and keep its index with it
        # Then sort the intervals
        # For each query go over the sorted intervals, (don't iterate over and over as it is already sorted)
        # while the interval start is less than equal to query, add it to min heap (length, end)
        # remove all the entries from min heap whose end is less than query
        # add first element of min heap to res in the index of the query
        intervals.sort()

        queries = [(q, i) for i, q in enumerate(queries)]

        queries.sort()

        res = [-1] * len(queries)
        minHeap = []
        j = 0
        for q, i in queries:
            while j < len(intervals) and intervals[j][0] <= q:
                length = intervals[j][1] - intervals[j][0] + 1
                heapq.heappush(minHeap, (length, intervals[j][1]))
                j += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[i] = minHeap[0][0] if minHeap else -1

        return res
            