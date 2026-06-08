class MedianFinder:

    def __init__(self):
       self.small = []
       self.large = [] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            item = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, item)

        if len(self.small) - len(self.large) > 1:
            item = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, item)

        if len(self.large) - len(self.small) > 1:
            item = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * item)

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 1:
            if len(self.small) > len(self.large):
                return -1 * self.small[0]
            else:
                return self.large[0]
        else:
            return float((-1 * self.small[0] + self.large[0]) / 2)
        