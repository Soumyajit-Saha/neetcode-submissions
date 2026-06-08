class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        prevOne = 1
        prevTwo = 2
        res = 0
        for i in range(3, n + 1):
            res = prevOne + prevTwo
            prevOne = prevTwo
            prevTwo = res

        return res