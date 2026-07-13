class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            if maxHeap:
                c = heapq.heappop(maxHeap)
                c = -c
                time += 1
                c = c - 1
                if c > 0:
                    q.append([c, time + n])
            else:
                time = q[0][1]

            if q and time == q[0][1]:
                c, _ = q.popleft()
                heapq.heappush(maxHeap, -c)

        return time