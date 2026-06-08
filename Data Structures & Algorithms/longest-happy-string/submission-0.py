class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                heapq.heappush(maxHeap, (-count, char))

        res = ""

        while maxHeap:
            count, c = heapq.heappop(maxHeap)
            count = -count
            if len(res) > 1 and res[-1] == res[-2] == c:
                    if maxHeap:
                        count2, c2 = heapq.heappop(maxHeap)
                        res += c2
                        count2 = -count2
                        count2 -= 1

                        if count2 > 0:
                            heapq.heappush(maxHeap, (-count2, c2))
                    else:
                        # Cannot put any char more
                        break
                    heapq.heappush(maxHeap, (-count, c))
            else:
                res += c
                count -= 1
                if count > 0:
                    heapq.heappush(maxHeap, (-count, c))

        return res




