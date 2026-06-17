class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        res = ""

        count = Counter(s)
        for c, count in count.items():
            maxHeap.append((-count, c))
        
        while maxHeap:
            count, c = heapq.heappop(maxHeap)
            count = -count
            if len(res) > 0 and res[-1] == c:
                if maxHeap:
                    count2, c2 = heapq.heappop(maxHeap)
                    count2 = -count2
                    res += c2
                    if count2 - 1 > 0:
                        heapq.heappush(maxHeap, (-count2 + 1, c2))
                    heapq.heappush(maxHeap, (-count, c))
                else:
                    return ""
            else:
                res += c
                if count - 1 > 0:
                    heapq.heappush(maxHeap, (-count + 1, c))
        
        return res
                