class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calc(power):
            if power == 0:
                return 1
            if power % 2 == 0:
                return calc(power // 2) * calc(power // 2)
            else:
                return x * calc(power // 2) * calc(power // 2)

        res = calc(abs(n))

        return res if n > 0 else 1 / res