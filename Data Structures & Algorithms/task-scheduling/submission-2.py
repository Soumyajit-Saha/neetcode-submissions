class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # put tasks count in a maxHeap
        # get the highest count task (greedy)
        # increment the time
        # put this task in queue with (curr time + idle time) to put it back in maxHeap when idle time is passed
        # this is done to add idle time between same tasks
        # if maxHeap is empty, proceed the time to next item in queue

        maxHeap = []
        countMap = Counter(tasks)

        for val in countMap.values():
            maxHeap.append(-1 * val)

        heapq.heapify(maxHeap)
        queue = deque()

        time = 0

        while maxHeap or queue:

            if not maxHeap:
                time = queue[0][1]
            else:
                time += 1
                count = -1 * heapq.heappop(maxHeap)

                count -= 1

                if count:
                    queue.append((count, time + n))

            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, -1 * queue.popleft()[0])

        return time

