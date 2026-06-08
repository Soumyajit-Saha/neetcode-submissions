class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Store count of all values.
        # Maintain a min Heap to get the lowest value
        # take the lowest value from the minHeap and check if all values from lowest value to lowest value + groupSize exists or not
        # when we go through one value, decrease the count by 1
        # Now if for a value the count got 0 and it is not the lowest value, that means there is a gap now, so return the False
        # Pop the lowest value from the min heap if its count goes to 0
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            
            for i in range(start, start + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
                if i == minHeap[0] and count[i] == 0:
                    heapq.heappop(minHeap)
                    print(minHeap)

        return True