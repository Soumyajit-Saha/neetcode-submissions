class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}

        def longest(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            while i > -1 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            dp[(i + 1, j - 1)] = s[i + 1: j]  
            return dp[(i + 1, j - 1)]
                
            

        res = ""
        for i in range(len(s)):
            res1 = longest(i, i)
            res2 = longest(i, i + 1) if i + 1 < len(s) else ""
            res3 = res1 if len(res1) > len(res2) else res2
            res = res if len(res) > len(res3) else res3

        return res
