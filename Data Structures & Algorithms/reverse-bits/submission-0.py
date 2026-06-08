class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            lastDigit = n & 1
            res = res << 1
            res = res | lastDigit

            n = n >> 1

        return res