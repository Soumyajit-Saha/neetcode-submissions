class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitsMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        comb = []
        def dfs(index):
            if index == len(digits):
                res.append(''.join(comb.copy()))
                return
            for c in digitsMap[digits[index]]:
                comb.append(c)
                dfs(index + 1)
                comb.pop()
        dfs(0)
        return res