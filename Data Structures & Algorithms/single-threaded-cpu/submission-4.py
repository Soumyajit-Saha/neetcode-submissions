class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minStart = []
        minProc = []
        res = []
        for i, (e, p) in enumerate(tasks):
            minStart.append([e, p, i])
        
        heapq.heapify(minStart)
        time = minStart[0][0]
        while minProc or minStart:
            while minStart and minStart[0][0] <= time:
                e, p, i = heapq.heappop(minStart)
                heapq.heappush(minProc, [p, i])
            if not minProc:
                time = minStart[0][0]
                continue
            p, i = heapq.heappop(minProc)
            time += p
            res.append(i)

        return res