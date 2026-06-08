class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j] == '0':
                return False
            elif abbr[j].isdigit():
                k = j
                num = 0
                while k < len(abbr) and abbr[k].isdigit():
                    num = num * 10 + int(abbr[k])
                    k += 1
                i += num
                j = k
            elif word[i] != abbr[j]:
                return False
            else:
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)

            