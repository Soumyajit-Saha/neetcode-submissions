class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        n = len(word)
        m = len(abbr)

        while i < n and j < m:
            if abbr[j].isdigit():
                num = 0
                k = j
                if abbr[j] == '0':
                    return False
                while k < m and abbr[k].isdigit():
                    num = num * 10 + int(abbr[k])
                    k += 1
                i += num
                j = k
            elif abbr[j] != word[i]:
                return False
            else:
                i += 1
                j += 1
        return True if i == n and j == m else False