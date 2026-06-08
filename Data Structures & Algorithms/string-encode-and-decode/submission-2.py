class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1
                res.append(s[i + 1: i + num + 1])
                i = i + num + 1

        return res
                
