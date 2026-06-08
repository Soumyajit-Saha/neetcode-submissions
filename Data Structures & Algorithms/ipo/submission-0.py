class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Two heaps: minCapital, maxProfit
        # Iterate k times
        #   First check from minCapital which is <= w
        #   put those profits in maxProfit
        #   Now add max profit from maxProfit to w

        minCapital = []
        maxProfit = []
        for i in range(len(capital)):
            minCapital.append((capital[i], profits[i]))

        heapq.heapify(minCapital)

        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            if not maxProfit:
                break
            
            prof = heapq.heappop(maxProfit)
            prof = -prof
            w += prof

        return w