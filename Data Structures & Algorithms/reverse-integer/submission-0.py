class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        res = 0
        while num != 0:
            d = num % 10
            res = res * 10 + d
            num = num // 10

        if res > (2**31 - 1) or res < (-2**31):
            return 0
        
        return res if x >= 0 else -res