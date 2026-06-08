class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        used = [] # end time, room
        available = [i for i in range(n)] # room
        count = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                last_end, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if not available:
                endtime, room = heapq.heappop(used)
                end = endtime + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))

            