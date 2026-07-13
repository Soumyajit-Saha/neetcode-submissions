class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        minCapital, maxProfit = [], []

        for i in range(len(profits)):
            minCapital.append([capital[i], profits[i]])
        
        heapq.heapify(minCapital)

        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            if not maxProfit:
                break

            p = heapq.heappop(maxProfit)
            p = -p
            w += p
        
        return w
