class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" == num1 or "0" == num2:
            return "0" 

        res = ""

        def add(n1, n2):
            n1 = n1[::-1]
            n2 = n2[::-1]

            i = 0
            j = 0
            carry = 0
            res = ""
            while i < len(n1) and j < len(n2):
                val = int(n1[i]) + int(n2[j]) + carry
                carry = val // 10
                val = val % 10
                res = str(val) + res
                i += 1
                j += 1

            while i < len(n1):
                val = int(n1[i]) + carry
                carry = val // 10
                val = val % 10
                res = str(val) + res
                i += 1

            while j < len(n2):
                val = int(n2[j]) + carry
                carry = val // 10
                val = val % 10
                res = str(val) + res
                j += 1

            if carry:
                res = str(carry) + res

            return res
            

        ten_multiplier = 0
        for n1 in num1[::-1]:
            carry = 0
            localRes = ""
            for n2 in num2[::-1]:
                val = int(n1) * int(n2) + carry
                carry = val // 10
                val = val % 10
                localRes = str(val) + localRes
            if carry:
                localRes = str(carry) + localRes
            zeroes = ''.join(['0'] * ten_multiplier)
            ten_multiplier += 1
            localRes = localRes + zeroes

            res = add(res, localRes)

        return res
                