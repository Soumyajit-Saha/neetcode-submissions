class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        roomToMeeting = {i: 0 for i in range(n)}

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                lastEnd, room = heapq.heappop(used)
                end = lastEnd + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            roomToMeeting[room] += 1
            heapq.heappush(used, [end, room])

        max_ = max(roomToMeeting.values())
        for i in range(n):
            if roomToMeeting[i] == max_:
                return i