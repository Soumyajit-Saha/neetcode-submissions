class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0

        index = {}
        res = 0

        for r in range(len(s)):
            if s[r] in index:
                print(index)
                conflictInd = index[s[r]]
                for i in range(l, conflictInd + 1):
                    index.pop(s[i], None)
                l = conflictInd + 1

            index[s[r]] = r
            res = max(res, r - l + 1)


        return res