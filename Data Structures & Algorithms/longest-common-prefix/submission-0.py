class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            minLen = min(len(prefix), len(strs[i]))
            newPrefix = ""
            j = 0
            while j < minLen:
                if prefix[j] != strs[i][j]:
                    if not newPrefix:
                        return ""
                else:
                    newPrefix += strs[i][j]
                j += 1
            prefix = newPrefix

        return prefix