class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            l = len(s)
            encodedStr += str(l) + '#' + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            if s[i].isdigit():
                l = ''
                while s[i] != '#':
                    l += s[i]
                    i += 1
                l = int(l)
                res.append(s[i + 1: i + l + 1])
                i = i + l + 1

        return res
