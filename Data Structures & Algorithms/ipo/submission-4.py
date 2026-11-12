class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        minCapital = [(capital[i], profits[i]) for i in range(n)]
        heapq.heapify(minCapital)
        maxProfit = []
        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)
            
            if not maxProfit:
                return w
            
            p = heapq.heappop(maxProfit)
            p = -p
            w += p

        return w