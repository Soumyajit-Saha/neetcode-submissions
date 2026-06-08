class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        res = 0

        for i in range(2, len(cost) + 1):
            if i == len(cost):
                res = min(first, second)
                break
            res = min(first + cost[i], second + cost[i])
            first = second
            second = res

        return res