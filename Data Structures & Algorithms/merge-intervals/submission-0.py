class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] > prevEnd:
                res.append(intervals[i])
            else:
                res[-1][1] = max(prevEnd, intervals[i][1])
            prevEnd = res[-1][1]
        return res