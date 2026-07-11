class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]
            if end < newInterval[0]:
                res.append([start, end])
            elif newInterval[1] < start:
                res.append(newInterval)
                res.extend(intervals[i: ])
                return res
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]

        res.append(newInterval)
        return res 