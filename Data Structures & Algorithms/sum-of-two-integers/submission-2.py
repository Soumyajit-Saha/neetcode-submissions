class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for i in range(32):
            lastA = a & 1
            lastB = b & 1
            currBit = lastA ^ lastB ^ carry
            if currBit:
                res = res | (1 << i)
            carry = (lastA + lastB + carry) >= 2
            a = a >> 1
            b = b >> 1

        if res > 0x7FFFFFFF:
            res = ~(res ^ 0xFFFFFFFF)
        return res