class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        charStack = []

        curr = ''
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '[':
                numStack.append(num)
                charStack.append(curr)
                curr = ''
                num = 0
            elif s[i] == ']':
                prevNum = numStack.pop()
                prev = charStack.pop()
                curr = prev + prevNum * curr
            else:
                curr += s[i]

        return curr