class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minStart, minProc = [], []

        for i, task in enumerate(tasks):
            task.append(i)
        
        minStart = tasks
        heapq.heapify(minStart)

        res = []

        time = minStart[0][0]

        while minStart or minProc:
            while minStart and time >= minStart[0][0]:
                _, proc, i = heapq.heappop(minStart)
                heapq.heappush(minProc, [proc, i])

            if not minProc:
                time = minStart[0][0]
                continue

            proc, i = heapq.heappop(minProc)
            time += proc
            res.append(i)



        return res