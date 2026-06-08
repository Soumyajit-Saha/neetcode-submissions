class Solution:
    def longestPalindrome(self, s: str) -> str:

        def longest(i, j):
            while i > -1 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            return s[i + 1: j]
                
            

        res = ""
        for i in range(len(s)):
            res1 = longest(i, i)
            res2 = longest(i, i + 1) if i + 1 < len(s) else ""
            res3 = res1 if len(res1) > len(res2) else res2
            res = res if len(res) > len(res3) else res3

        return res
