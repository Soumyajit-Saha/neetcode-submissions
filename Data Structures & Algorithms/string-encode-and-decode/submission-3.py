class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        return res
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            l = 0
            j = i
            while s[j] != '#':
                l = l * 10 + int(s[j])
                j += 1
            res.append(s[j + 1: j + 1 + l])
            i = j + 1 + l

        return res
            