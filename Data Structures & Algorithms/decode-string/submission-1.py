class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        k = 0
        curr = ''

        for c in s:
            if c.isdigit():
                # track digit as its own
                k = k * 10 + int(c)
            elif c == '[':
                count_stack.append(k)
                string_stack.append(curr)
                curr = ''
                k = 0
            elif c == ']':
                temp = curr
                count = count_stack.pop()
                prev = string_stack.pop()
                curr = prev + (temp * count)
            else:
                # track string as its own
                curr += c

        return curr


        
