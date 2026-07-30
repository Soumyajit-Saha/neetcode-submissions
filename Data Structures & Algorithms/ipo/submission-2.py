class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapital = [[capital[i], profits[i]] for i in range(len(capital))]
        maxProfit = []
        heapq.heapify(minCapital)

        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                _, profit = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -profit)

            if not maxProfit:
                return w

            profit = heapq.heappop(maxProfit)
            w += -profit

        return w
