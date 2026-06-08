class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff = 0
        res = 0

        for i in range(len(gas) - 1):
            diff += gas[i] - cost[i]

            if diff < 0:
                diff = 0
                res = i + 1

        return res