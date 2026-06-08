class Solution:
    def reorganizeString(self, s: str) -> str:
        # Idea is to get the most frequest char from max heap
        # reduce its count and put it on hold in prev (only if the count > 0)
        # (as we don not want to get it it even it is next most freq as it will be the same char)
        # in the next iteration of heap, get the next most frequent and push the prev

        # If prev is there but no element is in heap, return "" 
        # i.e, there is hold element and we cannot place any other char, and we have to place the same char again

        counter = Counter(s)

        maxHeap = [[-count, c] for c, count in counter.items()]
        heapq.heapify(maxHeap)

        res = ""

        while maxHeap:
            count, c = heapq.heappop(maxHeap)
            count = -count

            if len(res) > 0 and res[-1] == c:
                if maxHeap:
                    count2, c2 = heapq.heappop(maxHeap)
                    count2 = -count2

                    res += c2

                    count2 -= 1

                    if count2 > 0:
                        heapq.heappush(maxHeap, [-count2, c2])
                    heapq.heappush(maxHeap, [-count, c])
                else:
                    return ""

            else:
                res += c

                count -= 1

                if count > 0:
                    heapq.heappush(maxHeap, [-count, c])


        return res

            