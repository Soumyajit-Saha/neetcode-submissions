class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""

        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        while i >= 0 and j >= 0:
            bit = int(a[i]) + int(b[j]) + carry
            carry = bit // 2
            res = str(bit % 2) + res
            i -= 1
            j -= 1

        while i >= 0:
            bit = int(a[i]) + carry
            carry = bit // 2
            res = str(bit % 2) + res
            i -= 1

        while j >= 0:
            bit = int(b[j]) + carry
            carry = bit // 2
            res = str(bit % 2) + res
            j -= 1
        
        if carry:
            res = str(carry) + res

        return res