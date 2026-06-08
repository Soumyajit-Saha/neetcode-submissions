"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [intervals[i].start for i in range(len(intervals))]
        end = [intervals[i].end for i in range(len(intervals))]

        start.sort()
        end.sort()

        i = 0
        j = 0

        count = 0
        res = 0
        
        while i < len(start) and j < len(end):
            if start[i] < end[j]: # a meeting started
                count += 1
                i += 1
            else: # a meeting ended
                count -= 1
                j += 1
            res = max(res, count)

        while j < len(end):
            count -= 1
            res = max(res, count)
            j += 1

        return res

        


