class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        used = []
        available = [i for i in range(n)]
        rooms = {i: 0 for i in range(n)}

        meetings.sort()

        for start, end in meetings:
            while used and used[0][0] <= start:
                endTime, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                lastEnd, room = heapq.heappop(used)
                end = lastEnd + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, [end, room])
            rooms[room] += 1

        res = 0
        m = 0
        for room, count in rooms.items():
            if count > m:
                m = count
                res = room

        return res