class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        print(digits)
        res = []

        carry = 1
        for d in digits:
            val = d + carry
            carry = val // 10
            val = val % 10
            res.append(val)

        if carry:
            res.append(carry)

        return res[::-1]