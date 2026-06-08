class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = -1 * heapq.heappop(maxHeap)
            second = -1 * heapq.heappop(maxHeap)

            if first != second:
                heapq.heappush(maxHeap, -1 * (first - second))

        return -1 * maxHeap[0] if maxHeap else 0