class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def gcd(a, b):
            while a:
                a, b = b % a, a
            return b

        if str1 + str2 != str2 + str1:
            return ""

        g = gcd(len(str1), len(str2))
        return str1[:g]