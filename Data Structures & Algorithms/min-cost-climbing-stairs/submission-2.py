class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)

        prevOne = cost[0]
        prevTwo = cost[1]
        res = min(prevOne, prevTwo)

        for i in range(2, len(cost) + 1):
            if i == len(cost):
                res = 0 + min(prevOne, prevTwo)
            else:
                res = cost[i] + min(prevOne, prevTwo)
            prevOne = prevTwo
            prevTwo = res

        return res
