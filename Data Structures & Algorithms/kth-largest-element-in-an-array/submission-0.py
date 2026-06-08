class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-1 * num for num in nums]
        heapq.heapify(maxHeap)

        for i in range(1, k + 1):
            item = -1 * heapq.heappop(maxHeap)
            if i == k:
                return item
            