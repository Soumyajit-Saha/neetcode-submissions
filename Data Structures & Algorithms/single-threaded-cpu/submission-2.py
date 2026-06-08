class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Two heaps: minStart, minProc

        minStart = []
        minProc = []

        for i, task in enumerate(tasks):
            heapq.heappush(minStart, (task[0], task[1], i))

        time = 0
        res = []

        while minStart or minProc:
            while minStart and minStart[0][0] <= time:
                start, proc, i = heapq.heappop(minStart)
                heapq.heappush(minProc, (proc, i))

            if not minProc:
                time = minStart[0][0]
                continue
            
            procTime, i = heapq.heappop(minProc)
            time += procTime
            res.append(i)
        
        return res
