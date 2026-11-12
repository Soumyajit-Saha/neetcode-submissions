class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        minHeap = [k for k in count.keys()]
        heapq.heapify(minHeap)

        while minHeap:
            num = minHeap[0]
            for i in range(num, num + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0 and minHeap[0] == i:
                    heapq.heappop(minHeap)
        
        return True